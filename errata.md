# 正誤表

## 初版 第 1 刷

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

## 初版 第 2 刷

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

## その他

- 第 6 章
  - GitHub リポジトリ名が「streamlit-langchain-app」であり、Streamlit のタイトルが「langchain-streamlit-app」となっていますが、動作に影響はないため、このままの表記とします。

## 参考

正誤表の作成の際、以下の書評記事やお問い合わせを参考にさせていただきました。ありがとうございました。

- [ChatGPT/LangChain によるチャットシステム構築[実践]入門](https://zenn.dev/yoshii0110/articles/338af3e5123c68)
- [LLM を組み込んだチャットアプリケーションを写経しながら実装できる「ChatGPT/LangChain によるチャットシステム構築［実践］入門」を読んだ - kakakakakku blog](https://kakakakakku.hatenablog.com/entry/2023/10/16/085525)
