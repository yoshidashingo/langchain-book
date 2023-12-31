import os

from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

# ボットトークンを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))

# ソケットモードハンドラーを使ってアプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
