

from pathlib import Path
import requests
import toml

credentials_path = Path(__file__).parent.parent.joinpath("config").joinpath('telegram.toml')
config = toml.load(credentials_path)

bot_token = config['botToken']
chat_id = config['chatId']

def send_telegram_notification(message):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {"chat_id": chat_id, "text": message}
    response = requests.post(url, json=payload)
    return response.json()

if __name__ == "__main__":
    send_telegram_notification("""Hemos actualizado la tabla de inmuebles 🐋. 
----------------------------
Puedes mirar el enlace para alquileres 🔑: https://docs.google.com/spreadsheets/d/1FmdB_RnVX-sibai32bHg-DVTLtMmBHBsbobxBIHqNQ4/edit?usp=sharing
-----------------------------
Puedes mirar el enlace para ventas 🏠: https://docs.google.com/spreadsheets/d/1SoAkDnF92fTOQgUjjb7dgtQ5Asvmy6WvJrt9G37K2mo/edit?usp=drive_link 
-----------------------------                         
                               """)