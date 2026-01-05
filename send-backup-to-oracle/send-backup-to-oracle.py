### Código gerado pelo ChatGPT e adaptado pelo Github Copilot ###
#### Adaptado por hssj.dev.br ####
#### Adaptado para Oracle Cloud Object Storage ####
import oci
from oci.object_storage import ObjectStorageClient

def enviar_arquivo_para_oracle(arquivo, manter_arquivo):
    import os

    # Configurações da Oracle Cloud
    config_file_path = os.getenv('OCI_CONFIG_FILE', os.path.expanduser('~/.oci/config'))
    config_profile = os.getenv('OCI_CONFIG_PROFILE', 'DEFAULT')
    namespace = os.getenv('OCI_NAMESPACE')
    bucket_name = os.getenv('OCI_BUCKET')

    # Carrega a configuração da Oracle Cloud
    config = oci.config.from_file(config_file_path, config_profile)
    client = ObjectStorageClient(config)
    
    object_name = arquivo

    # Obtém o prefixo do arquivo
    arquivo_prefixo = arquivo.split('-')[0]

    # Liste todos os objetos no bucket
    try:
        objects = client.list_objects(namespace, bucket_name, prefix=arquivo_prefixo.lstrip('/'))
    except Exception as e:
        print(f"Erro ao listar objetos: {e}")
        return

    # Crie um dicionário para armazenar os nomes dos arquivos e suas datas
    file_dates = {}

    for obj in objects.data:
        file_name = obj.name
        # Extraia a data do nome do arquivo (assumindo que o formato é "backup-YYYY-MM-DD.tar.bz2")
        date_str = file_name.split("-", 1)[1]
        file_dates[file_name] = date_str

    # Ordene os arquivos pelo nome (que inclui a data)
    sorted_files = sorted(file_dates.items(), key=lambda x: x[0])

    # Exclua o arquivo mais antigo
    if sorted_files and not manter_arquivo:
        oldest_file_name, _ = sorted_files[0]
        try:
            client.delete_object(namespace, bucket_name, oldest_file_name)
            print(f"Arquivo mais antigo ({oldest_file_name}) excluído com sucesso.")
        except Exception as e:
            print(f"Erro ao excluir arquivo: {e}")
    else:
        print("Nenhum arquivo encontrado.")
    
    # Realizando o envio do novo arquivo
    try:
        with open(arquivo, 'rb') as file:
            client.put_object(namespace, bucket_name, object_name, os.path.getsize(arquivo), file)
        print(f"Arquivo {arquivo} enviado com sucesso para o Oracle Cloud Object Storage.")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o Oracle Cloud: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 3:
        print("Uso: python send-backup-to-oracle.py <arquivo> [--keep | --nokeep]")
        sys.exit(1)
        
    arquivo = sys.argv[1]
    manter_arquivo = None
    if sys.argv[2] == '--keep':
        manter_arquivo = True
    else:
        manter_arquivo = False

    enviar_arquivo_para_oracle(arquivo, manter_arquivo)