import os
import re

from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

load_dotenv()

# ボットトークンを使ってアプリを初期化します
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


@app.event("app_mention")
def handle_mention(event, say):
    thread_ts = event["ts"]
    message = re.sub("<@.*>", "", event["text"])

    llm = ChatOpenAI(
        model_name=os.environ["OPENAI_API_MODEL"],
        temperature=os.environ["OPENAI_API_TEMPERATURE"],
    )

    response = llm.predict(message)
    say(text=response, thread_ts=thread_ts)


# ソケットモードハンドラーを使ってアプリを起動します
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()
