import traceback
import os
from django.core.management.base import BaseCommand
from minio import Minio
import logging
import sys
import logging_loki

class Command(BaseCommand):
    help = 'Send file to MinIO and manage old files'

    def add_arguments(self, parser):
        parser.add_argument(
            '--config',
            type=str,
            help='Path to the MinIO configuration file'
        )
        parser.add_argument(
            '--file',
            type=str,
            help='Path to the file to be sent to MinIO'
        )
        parser.add_argument(
            '--keep',
            type=int, default=0,
            help='Keep the oldest file in MinIO'
        )

    def _load_config(self, config_file):
        """Load configuration from a file."""
        config = {}
        try:
            with open(config_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    # Ignora linhas vazias e comentários
                    if line and not line.startswith('#'):
                        if '=' in line:
                            key, value = line.split('=', 1)
                            config[key.strip()] = value.strip()
            return config
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file not found: {config_file}")
        except Exception as e:
            raise ValueError(f"Error on reading config file {config_file}: {str(e)}")
        

    def _log_messages(self, log_server_url, message, level='info', minio_bucket=None):
        # Check if Loki logging is configured
        if log_server_url:
            logger = logging.getLogger(f'send-to-minio-{minio_bucket}')
            logger.setLevel(logging.INFO)

            loki_handler = logging_loki.LokiHandler(
                url=log_server_url,
                tags={"application": "send-to-minio"},
                version="1",
            )

            # Formatter for logs
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            loki_handler.setFormatter(formatter)

            logger.addHandler(loki_handler)

            if level == 'info':
                logger.info(message)
            elif level == 'error':
                logger.error(message)
            elif level == 'warning':
                logger.warning(message)
            elif level == 'debug':
                logger.debug(message)
            else:
                logger.info(message)
        else:
            # Caso não esteja configurado, não faz nada
            return

    

    def handle(self, *args, **options):
        try:
            # Carrega configurações do arquivo .env ou variáveis de ambiente
            if options['config']:
                config = self._load_config(options['config'])
                minio_host = config.get('MINIO_HOST')
                minio_access_key = config.get('MINIO_ACCESS_KEY')
                minio_secret_key = config.get('MINIO_SECRET_KEY')
                minio_bucket = config.get('MINIO_BUCKET')
                loki_server_url = config.get('LOKI_SERVER_URL')
            else:
                minio_host = os.getenv('MINIO_HOST')
                minio_access_key = os.getenv('MINIO_ACCESS_KEY')
                minio_secret_key = os.getenv('MINIO_SECRET_KEY')
                minio_bucket = os.getenv('MINIO_BUCKET')
                loki_server_url = os.getenv('LOKI_SERVER_URL')

            # Validação das configurações
            if not all([minio_host, minio_access_key, minio_secret_key, minio_bucket]):
                raise ValueError('Incomplete config: MINIO_HOST, MINIO_ACCESS_KEY, MINIO_SECRET_KEY and MINIO_BUCKET are required.')

            client = Minio(minio_host,
                        access_key=minio_access_key,
                        secret_key=minio_secret_key,
                        secure=False)
            
            bucket_name = minio_bucket
            object_name = options['file']

            # Obtém o prefixo do arquivo
            arquivo_prefixo = object_name.split('-')[0]

            # Liste todos os objetos no bucket
            objects = client.list_objects(bucket_name, prefix=arquivo_prefixo.lstrip('/'), recursive=True)

            # Crie um dicionário para armazenar os nomes dos arquivos e suas datas
            file_dates = {}

            for obj in objects:
                file_name = obj.object_name
                # Extraia a data do nome do arquivo (assumindo que o formato é "backup-YYYY-MM-DD.tar.bz2")
                date_str = file_name.split("-", 1)[1]
                file_dates[file_name] = date_str

            # Ordene os arquivos pelo nome (que inclui a data)
            sorted_files = sorted(file_dates.items(), key=lambda x: x[0])

            # Remove arquivos antigos, mantendo apenas os últimos 'keep' arquivos
            keep_count = options['keep']
            if keep_count > 0:
                if len(sorted_files) > keep_count:
                    files_to_remove = len(sorted_files) - keep_count
                    for i in range(files_to_remove):
                        file_to_remove, _ = sorted_files[i]
                        client.remove_object(bucket_name, file_to_remove)
                        self.stdout.write(self.style.SUCCESS(f"Old file ({file_to_remove}) deleted successfully."))
                        self._log_messages(loki_server_url, f"Old file ({file_to_remove}) deleted successfully.", level='info', minio_bucket=minio_bucket)
                    self.stdout.write(self.style.SUCCESS(f"Total of {files_to_remove} old file(s) removed, keeping {keep_count} file(s)."))
                    self._log_messages(loki_server_url, f"Total of {files_to_remove} old file(s) removed, keeping {keep_count} file(s).", level='info', minio_bucket=minio_bucket)
                else:
                    self.stdout.write(self.style.WARNING(f"Number of files ({len(sorted_files)}) is less than or equal to the number to keep ({keep_count})."))
                    self._log_messages(loki_server_url, f"Number of files ({len(sorted_files)}) is less than or equal to the number to keep ({keep_count}).", level='warning', minio_bucket=minio_bucket)
            else:
                self.stdout.write(self.style.WARNING("No files will be removed (--keep=0)."))
                self._log_messages(loki_server_url, "No files will be removed (--keep=0).", level='warning', minio_bucket=minio_bucket)

            # Enviar o arquivo
            client.fput_object(bucket_name, object_name, object_name)
            self.stdout.write(self.style.SUCCESS(f"File {object_name} sent successfully to MinIO."))
            self._log_messages(loki_server_url, f"File {object_name} sent successfully to MinIO.", level='info', minio_bucket=minio_bucket) 
                
        except Exception as e:
            traceback.print_exc()
            self.stderr.write(self.style.ERROR(f'Error to send files to MinIO: {e}'))
            self._log_messages(loki_server_url, f'Error to send files to MinIO: {e}', level='error', minio_bucket=minio_bucket)
            return