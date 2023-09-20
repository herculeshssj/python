import os
import subprocess
from discord_webhook import DiscordWebhook

"""
Alerta via Discord quando a conexão com o Raspberry PI caiu

Dica obtida de https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
"""

if __name__ == '__main__':
    # Obtém as variáveis de ambiente
    discord_url = os.getenv('DISCORD_URL')
    ip_check = os.getenv('IP_CHECK')
    port_check = os.getenv('PORT_CHECK')


    # Executa o comando nc
    result = subprocess.run(['nc', '-z', '-v', ip_check, port_check], stdout=subprocess.PIPE)
    print(result)

    if "returncode=0" in str(result):
        print('VPN up! :)')
    else:
        print('VPN down :(')

        # Constrói a mensagem
        mensagem_discord = 'VPN caiu! Verifique a conexão com o Raspberry PI...'
        
        # Envia a mensagem de aviso
        print(mensagem_discord) # Impressão no console, para fins de debug.
        webhook = DiscordWebhook(url=discord_url, content=mensagem_discord)
        response = webhook.execute()
