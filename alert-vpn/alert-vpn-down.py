import requests, json
import os, sys
import subprocess
from datetime import datetime, timedelta
from discord_webhook import DiscordWebhook

"""
Alerta via Discord quando a conexão com o Raspberry PI caiu
"""

if __name__ == '__main__':
    # Executa o comando nc
    result = subprocess.run(['nc', '-z', '-v', '192.168.66.2', '2000'], stdout=subprocess.PIPE)
    print(result)

    """
    #discord_url = ''
    discord_url = os.getenv('DISCORD_URL')

    # Constrói a mensagem
    mensagem_discord = 'VPN caiu! Verifique a conexão com o Raspberry PI...'
    
    # Envia a mensagem de aviso
    print(mensagem_discord) # Impressão no console, para fins de debug.
    webhook = DiscordWebhook(url=discord_url, content=mensagem_discord)
    response = webhook.execute()
"""