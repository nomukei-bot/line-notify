import os
import requests

LINE_TOKEN = os.getenv("LINE_TOKEN")

def send_line_message(message: str):
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "Authorization": f"Bearer {LINE_TOKEN}",
    }
    data = {
        "message": message,
    }
    response = requests.post("https://notify-api.line.me/api/notify", headers=headers, data=data)
    response.raise_for_status()

if __name__ == "__main__":
    send_line_message("【物件チェック】テスト実行しました。（まだ条件判定ロジックはこれから作るよ）")
