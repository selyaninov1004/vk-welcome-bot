
from flask import Flask, request
import json
import requests

app = Flask(__name__)

GROUP_TOKEN = "vk1.a.9KdmzVfgeuj8We1TRNniATbwaAyt_XG7LJX5JPGQBEaNmI9xeoVSTel6oX-56MokKCR7r_0odhT4dPAFa0eFAtIQcfbQMhuCrbmEiamehEI6N6n1gFaqVviA6pXa2m4EPKhXHyB8kPsy-QV5GPjfXpyv3zuCcOCePvzzFlszDp3Z3HZDC86YUGy2rXTWUPaPXjcZ_TifLC4vquvxAaEsXQ"
CONFIRMATION_TOKEN = "e18dd0c6"
WELCOME_LINK = "https://www.asu.ru/"

@app.route("/", methods=["POST"])
def vk_bot():
    data = request.json

    if data["type"] == "confirmation":
        return CONFIRMATION_TOKEN

    if data["type"] == "group_join":
        user_id = data["object"]["user_id"]
        send_message(user_id, f"Привет! Спасибо за подписку 😊 Вот ссылка: {WELCOME_LINK}")
        return "ok"

    return "ok"

def send_message(user_id, message):
    requests.post("https://api.vk.com/method/messages.send", params={
        "user_id": user_id,
        "message": message,
        "random_id": 0,
        "access_token": GROUP_TOKEN,
        "v": "5.131"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
