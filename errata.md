# 正誤表

## 初版 第 1 刷 (第 2 刷で修正)

- p82 本文 3 行目, 5 行目, p84 最終行
  - 誤) Recepi
  - 正) Recipe
- p104「Vector stores」の項の最後の一文
  - 誤) ElasticSearch
  - 正) Elasticsearch
- p156 図 7.1
  - 誤) AWS-Lambda
  - 正) AWS Lambda
- p183 ソースコード 4 行目
  - 正) `self.interval = CHAT_UPDATE_INTERVAL_SEC` を強調 (青字)
- p250 ~/.bashrc に pyenv を使用するための設定を追加
  ```diff
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' \
  - >> ~/. bashrc
  + >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  ```

## 初版 第 2 刷 (第 3 刷で修正)

- p120 図 5.13
  - 誤) 東京都大阪の天気を教えて
  - 正) 東京と大阪の天気を教えて
- p161 7.3「環境設定ファイルを作成する」1 行目
  - 誤) .env.template
  - 正) .env.example
- p249 コマンド 1 行目
  - 誤) `git clone git@github.com:os1ma/langchain-book.git`
  - 正) `git clone git@github.com:<GitHubのユーザー名>/langchain-book.git`
  - 【補足】このコマンドは「langchain-book」という名前のリポジトリを作成した場合の例です。リポジトリ名が異なる場合は、「langchain-book」の箇所を作成したリポジトリ名に置き換えてください。

### パッケージのバージョン固定に関する変更

初版 第 2 刷までは、本文中でパッケージのバージョンを固定しておらず、パッケージのバージョンアップに起因するエラーが発生する場合がありました。
そこで第 3 刷からはパッケージのバージョンを固定するよう、以下の箇所を変更しました。

- p vii「使用しているソフトウェアのバージョン」本文 7 行目
  - 旧) そのため、本文中で各種パッケージをインストールする箇所では、明示的にバージョンを指定していません。バージョンの違いによってうまく動作しない場合は、<以後略>
  - 新) ただし、本書ではソースコードの動作を確実にするため、本文中で各種パッケージをインストールする箇所で、明示的にバージョンを指定しています。それでもバージョンの違いによってうまく動作しない場合は、<以後略>
- p55 OpenAI のライブラリをインストールするコマンド
  - 旧) `!pip install openai`
  - 新) `!pip install openai==0.28.0`
- p73 LangChain をインストールするコマンド
  - 旧) `!pip install langchain openai`
  - 新) `!pip install langchain==0.0.292 openai==0.28.0`
- p101 GitPython をインストールするコマンド
  - 旧) `!pip install GitPython`
  - 新) `!pip install GitPython==3.1.36`
- p103 tiktoken をインストールするコマンド
  - 旧) `!pip install tiktoken`
  - 新) `!pip install tiktoken==0.5.1`
- p104 Chroma をインストールするコマンド
  - 旧) `!pip install chromadb`
  - 新) `!pip install chromadb==0.4.10`
- p118 DuckDuckGo のクライアントをインストールするコマンド
  - 旧) `!pip install duckduckgo-search`
  - 新) `!pip install duckduckgo-search==3.8.5`
- p134 Streamlit をインストールするコマンド
  - 旧) `pip install streamlit`
  - 新) `pip install streamlit==1.26.0`
- p141 LangChain などをインストールするコマンド
  - 旧) `pip install langchain openai python-dotenv`
  - 新) `pip install langchain==0.0.292 openai==0.28.0 python-dotenv==1.0.0`
- p143 DuckDuckGo と Wikipedia のクライアントをインストールするコマンド
  - 旧) `pip install duckduckgo-search wikipedia`
  - 新) `pip install duckduckgo-search==3.8.5 wikipedia==1.4.0`
- p170 Slack Bolt for Python などをインストールするコマンド
  - 旧) `$ pip install slack_bolt python-dotenv`
  - 新) `$ pip install slack_bolt==1.18.0 python-dotenv==1.0.0`
- p174 LangChain などをインストールするコマンド
  - 旧) `$ pip install langchain openai`
  - 新) `$ pip install langchain==0.0.292 openai==0.28.0`
- p178 Momento のクライアントをインストールするコマンド
  - 旧) `$ pip install momento`
  - 新) `$ pip install momento==1.9.2`
- p181 Boto3 をインストールするコマンド
  - 旧) `$ pip install boto3`
  - 新) `$ pip install boto3==1.28.49`
- p186 Serverless Framework をインストールするコマンド
  - 旧) `$ npm install -g serverless`
  - 新) `$ npm install -g serverless@3.35.2`
- p187 Serverless Framework のプラグインをインストールするコマンド
  - 旧)
    ```
    $ serverless plugin install -n serverless-python-requirements
    $ serverless plugin install -n serverless-dotenv-plugin
    ```
  - 新)
    ```
    $ serverless plugin install -n serverless-python-requirements@6.0.0
    $ serverless plugin install -n serverless-dotenv-plugin@6.0.0
    ```
- p210 Pinecone のクライアントなどをインストールするコマンド
  - 旧) `$ pip install pinecone-client tiktoken`
  - 新) `$ pip install pinecone-client==2.2.4 tiktoken==0.5.1`
- p210 PDF の読み込みに必要なパッケージをインストールするコマンド
  - 旧) `$ pip install unstructured pdf2image pdfminer.six`
  - 新) `$ pip install unstructured==0.10.15 pdf2image==1.16.3 pdfminer.six==20221105`

## その他

- 第 6 章
  - GitHub リポジトリ名が「streamlit-langchain-app」であり、Streamlit のタイトルが「langchain-streamlit-app」となっていますが、動作に影響はないため、このままの表記とします。
- 第 6 章から第 8 章
  - 第 6 章ではコマンドの先頭に `$` がついていませんが、第 7 章と第 8 章は `$` がついています。動作に影響はないため、このままの表記とします。

## 参考

正誤表の作成の際、以下の書評記事やお問い合わせを参考にさせていただきました。ありがとうございました。

- [ChatGPT/LangChain によるチャットシステム構築[実践]入門](https://zenn.dev/yoshii0110/articles/338af3e5123c68)
- [LLM を組み込んだチャットアプリケーションを写経しながら実装できる「ChatGPT/LangChain によるチャットシステム構築［実践］入門」を読んだ - kakakakakku blog](https://kakakakakku.hatenablog.com/entry/2023/10/16/085525)
