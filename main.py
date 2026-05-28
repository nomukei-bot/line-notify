import os
import requests
import json

CHANNEL_ACCESS_TOKEN = os.getenv("LINE_TOKEN")
USER_ID = os.getenv("LINE_USER_ID")  # ← 後で GitHub Secrets に追加する

def send_line_message(message: str):
    url = "https://api.line.me/v2/bot/message/push"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {CHANNEL_ACCESS_TOKEN}",
    }

    data = {
        "to": USER_ID,
        "messages": [
            {"type": "text", "text": message}
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))
    response.raise_for_status()

if __name__ == "__main__":
    send_line_message("【物件チェック】テスト実行しました。（Messaging API版）")
