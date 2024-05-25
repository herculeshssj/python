### Código gerado pelo ChatGPT ###
### Adaptador por hssj.dev.br ####
from minio import Minio

def enviar_arquivo_para_minio(arquivo):
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
    
    try:
        client.fput_object(bucket_name, object_name, arquivo)
        print(f"Arquivo {arquivo} enviado com sucesso para o MinIO.")
    except Exception as e:
        print(f"Erro ao enviar o arquivo para o MinIO: {e}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) != 2:
        print("Uso: python enviar_para_minio.py <arquivo>")
        sys.exit(1)
        
    arquivo = sys.argv[1]
    enviar_arquivo_para_minio(arquivo)