### Código gerado pelo ChatGPT ###
#### Adaptado por hssj.dev.br ####
from minio import Minio

def enviar_arquivo_para_minio(arquivo, manter_arquivo):
    import os

    minio_host = os.getenv('MINIO_HOST')
    minio_access_key = os.getenv('MINIO_ACCESS_KEY')
    minio_secret_key = os.getenv('MINIO_SECRET_KEY')
    minio_bucket = os.getenv('MINIO_BUCKET')

    client = Minio(minio_host,
                   access_key=minio_access_key,
                   secret_key=minio_secret_key,
                   secure=False)
    
    bucket_name = minio_bucket
    object_name = arquivo

    # Obtém o prefixo do arquivo
    arquivo_prefixo = arquivo.split('-')[0]

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

    # Exclua o arquivo mais antigo
    if sorted_files and not manter_arquivo:
        oldest_file_name, _ = sorted_files[0]
        client.remove_object(bucket_name, oldest_file_name)
        print(f"Arquivo mais antigo ({oldest_file_name}) excluído com sucesso.")
    else:
        print("Nenhum arquivo encontrado.")
    
    # Realizando o envio do novo arquivo
    try:
        client.fput_object(bucket_name, object_name, arquivo)
        print(f"Arquivo {arquivo} enviado com sucesso para o MinIO.")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o MinIO: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Uso: python enviar_para_minio.py <arquivo> [--keep | --nokeep]")
        sys.exit(1)
        
    arquivo = sys.argv[1]
    manter_arquivo = None
    if sys.argv[2] == '--keep':
        manter_arquivo = True
    else:
        manter_arquivo = False

    enviar_arquivo_para_minio(arquivo, manter_arquivo)