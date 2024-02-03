# アップデート

## LangChain v0.1 に対応したソースコードの追加

LangChain v0.1 に対応したソースコードを [langchain-v0.1 ブランチ](https://github.com/yoshidashingo/langchain-book/tree/langchain-v0.1) に追加しました。

### 主な変更点

書籍上 (main ブランチ) のソースコードとの主な変更点は以下の通りです。

- openai v1 での変更に対応
- Chat Completions API の functions の非推奨化に対応（新たに推奨されるようになった tools を使用するようにしました）
- langchain v0.1 での変更に対応
- pinecone-client v3 での変更に対応

特に LangChain については、以下の大きなアップデートに対応したソースコードとなっています。

- langchain という 1 つのパッケージから、langchain-core・langchain・langchain-openai・langchain-community・langchain-experimental などのパッケージに分割されたこと
- 2023 年 10 月後半頃から、「LangChain Expression Language (LCEL)」を使う実装が標準的となったこと

LangChain のこれらのアップデートについては、以下のスライド・記事に概要をまとめているので、参考にしてください。

- [速習：LangChain の大きなアップデート（2023 年秋〜冬）](https://speakerdeck.com/os1ma/su-xi-langchainnoda-kinaatupudeto-2023nian-qiu-dong)
- [LangChain の新記法「LangChain Expression Language (LCEL)」入門](https://zenn.dev/os1ma/articles/acd3472c3a6755)

### 各章のソースコード

v0.1 に対応した各章のソースコードは以下を参照してください。

| 章                                                                  | ソースコード                                                                                |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------- |
| 第 3 章 ChatGPT を API から利用するために                           | https://github.com/yoshidashingo/langchain-book/blob/langchain-v0.1/chapter3/notebook.ipynb |
| 第 4 章 LangChain の基礎                                            | https://github.com/yoshidashingo/langchain-book/blob/langchain-v0.1/chapter4/notebook.ipynb |
| 第 5 章 LangChain の活用                                            | https://github.com/yoshidashingo/langchain-book/blob/langchain-v0.1/chapter5/notebook.ipynb |
| 第 6 章 外部検索、履歴を踏まえた応答をする Web アプリの実装         | https://github.com/yoshidashingo/langchain-book/blob/langchain-v0.1/chapter6                |
| 第 7 章 ストリーム形式で履歴を踏まえた応答をする Slack アプリの実装 | https://github.com/yoshidashingo/langchain-book/tree/langchain-v0.1/chapter7                |
| 第 8 章 社内文書に答える Slack アプリの実装                         | https://github.com/yoshidashingo/langchain-book/tree/langchain-v0.1/chapter8                |

書籍との差分は [こちら](https://github.com/yoshidashingo/langchain-book/compare/main..langchain-v0.1) から確認できます。

### 動作確認したバージョン

Python や環境については、書籍と同じ条件で動作確認しました。

各 Python パッケージの動作確認済みバージョンは、各章のディレクトリの requirements.txt や requirements.lock などを参照してください。

なお、主要なパッケージは以下のバージョンで動作確認しました。

- openai==1.10.0
- langchain-core==0.1.18
- langchain==0.1.5
- langchain-openai==0.0.5
- langchain-community==0.0.17
