import requests
from requests.auth import HTTPBasicAuth

# Configurações
WP_URL = "https://hssj.dev.br/wp-json/wp/v2/posts"
WP_USER = "SEU_USUARIO"  # Substitua pelo seu usuário WordPress
WP_APP_PASSWORD = "SENHA_DE_APLICATIVO"  # Substitua pela senha de aplicativo gerada

# Dados do novo post
post = {
    "title": "Título do Post via API",
    "content": "Conteúdo do post criado via REST API.",
    "status": "publish"  # ou 'draft' para rascunho
}

if __name__ == '__main__':
    response = requests.post(
        WP_URL,
        auth=HTTPBasicAuth(WP_USER, WP_APP_PASSWORD),
        json=post
    )
    if response.status_code == 201:
        print("Post criado com sucesso!")
        print("URL:", response.json().get("link"))
    else:
        print("Erro ao criar post:", response.status_code)
        print(response.text)