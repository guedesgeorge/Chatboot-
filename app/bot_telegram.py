from flask import Flask, request
import requests
import os
from chatbot_base import ChatbotLicitacao

app = Flask(__name__)
bot = ChatbotLicitacao()

TELEGRAM_TOKEN = "8741462073:AAEWi1w-pTYmzQV3R70HtSxWqmkaEVevTPg"
TELEGRAM_API = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}"

@app.route('/webhook', methods=['POST'])
def telegram_webhook():
    data = request.json
    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')
        
        # Processar com o bot
        resposta = bot.processar_mensagem(text)
        
        # Enviar resposta
        requests.post(f"{TELEGRAM_API}/sendMessage", json={
            'chat_id': chat_id,
            'text': resposta
        })
    return 'OK'

@app.route('/')
def home():
    return '✅ Bot Telegram Licitações - Online!'

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8080))
    app.run(host='0.0.0.0', port=port)
