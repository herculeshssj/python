import os
import subprocess
import requests

"""
Alerta via Telegram quando a conexão com o Raspberry PI caiu

Dica obtida de https://stackoverflow.com/questions/4760215/running-shell-command-and-capturing-the-output
"""

if __name__ == '__main__':
    # Obtém as variáveis de ambiente
    telegram_token = os.getenv('TELEGRAM_TOKEN')
    telegram_chat_id = os.getenv('TELEGRAM_CHAT_ID')
    ip_check = os.getenv('IP_CHECK')
    port_check = os.getenv('PORT_CHECK')
    mensagem_telegram = os.getenv('ERROR_MESSAGE')

    # Executa o comando nc
    result = subprocess.run(['nc', '-z', '-v', ip_check, port_check], stdout=subprocess.PIPE)
    print(result)

    if result.returncode == 0:
        print('VPN up! :)')
    else:
        print('VPN down :(')

        # Envia a mensagem de aviso via Telegram
        print(mensagem_telegram)  # Impressão no console, para fins de debug.
        url = f"https://api.telegram.org/bot{telegram_token}/sendMessage"
        payload = {
            "chat_id": telegram_chat_id,
            "text": mensagem_telegram
        }
        response = requests.post(url, data=payload)
        print(response.text)
