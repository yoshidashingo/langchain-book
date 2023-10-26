# 正誤表

## 初版 第 1 刷

- p104「Vector stores」の項の最後の一文
  - 誤) ElasticSearch
  - 正) Elasticsearch
- p156 図 7.1
  - 誤) AWS-Lambda
  - 正) AWS Lambda
- p183 ソースコード 4 行目
  - 正) `self.interval = CHAT_UPDATE_INTERVAL_SEC` を強調 (青字)
- p250 ~/.bashrc に pyenv を使用するための設定
  ```diff
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' \
  -  >> ~/. bashrc
  +  >> ~/.bashrc
  echo 'eval "$(pyenv init -)"' >> ~/.bashrc
  ```

## その他

- 第 6 章
  - GitHub リポジトリ名が「streamlit-langchain-app」であり、Streamlit のタイトルが「langchain-streamlit-app」となっていますが、動作に影響はないため、このままの表記とします。

## 参考

正誤表の作成の際、以下の書評記事を参考にさせていただきました。ありがとうございました。

- [ChatGPT/LangChain によるチャットシステム構築[実践]入門](https://zenn.dev/yoshii0110/articles/338af3e5123c68)
- [LLM を組み込んだチャットアプリケーションを写経しながら実装できる「ChatGPT/LangChain によるチャットシステム構築［実践］入門」を読んだ - kakakakakku blog](https://kakakakakku.hatenablog.com/entry/2023/10/16/085525)
