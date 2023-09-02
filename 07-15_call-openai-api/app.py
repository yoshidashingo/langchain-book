import os
import re

import openai
from dotenv import load_dotenv
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

openai.api_key = os.environ["OPENAI_API_KEY"]

# ボットトークンとソケットモードハンドラーを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.event("app_mention")
def handle_mention(event, say):
    thread_ts = event["ts"]
    message = re.sub("<@.*>", "", event["text"])
    response = openai.ChatCompletion.create(
        model=os.environ["OPENAI_API_MODEL"],
        messages=[
            {"role": "user", "content": message},
        ],
        temperature=float(os.environ["OPENAI_API_TEMPERATURE"]),
    )
    say(thread_ts=thread_ts, text=response.choices[0]["message"]["content"].strip())


# アプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
