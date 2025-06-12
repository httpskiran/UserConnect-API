import os
import requests
from .models import TelegramUser

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
BASE_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def get_updates():
    response = requests.get(f"{BASE_URL}/getUpdates")
    return response.json()

def handle_start_command():
    updates = get_updates()
    for update in updates.get("result", []):
        message = update.get("message", {})
        chat = message.get("chat", {})
        text = message.get("text", "")
        username = chat.get("username")

        if text == "/start" and username:
            TelegramUser.objects.get_or_create(telegram_username=username)
            send_message(chat_id=chat["id"], text="Welcome! Your username has been saved.")

def send_message(chat_id, text):
    url = f"{BASE_URL}/sendMessage"
    data = {"chat_id": chat_id, "text": text}
    requests.post(url, data=data)
