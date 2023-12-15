# ChatGPT、LangChain によるチャットシステム構築［実践］入門

「ChatGPT、LangChain によるチャットシステム構築［実践］入門」の GitHub リポジトリです。

https://www.amazon.co.jp/dp/4297138395

> [!WARNING]
> 本書で使用しているパッケージは非常にアップデートが激しいため、バージョンの違いに起因するエラーに遭遇する可能性があります。
> とくに `pip install` でパッケージをインストールする際は、動作確認済みのバージョンを使用するようにしてください。
> 具体的なコマンドは「[パッケージのバージョン固定に関する変更](errata.md#%E3%83%91%E3%83%83%E3%82%B1%E3%83%BC%E3%82%B8%E3%81%AE%E3%83%90%E3%83%BC%E3%82%B8%E3%83%A7%E3%83%B3%E5%9B%BA%E5%AE%9A%E3%81%AB%E9%96%A2%E3%81%99%E3%82%8B%E5%A4%89%E6%9B%B4)」を参照してください。

> [!WARNING]
> 本書の一部で使用しているパッケージ「duckduckgo-search」のバージョン 3.8.5 が 2023 年 12 月頃から動作しなくなりました。
> （使用すると `HTTPError` というエラーが発生します）
> バージョン 4.1.0 は動作することを確認できたので、duckduckgo-search はバージョン 4.1.0 を使用してください。
> なお、このリポジトリで公開している Google Colab の該当箇所や requirements.txt は更新済みです。

## 各章のソースコード

| 章                                                                  | Colab                                                                                                                                                                                 |
| ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 第 3 章 ChatGPT を API から利用するために                           | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yoshidashingo/langchain-book/blob/main/chapter3/notebook.ipynb) |
| 第 4 章 LangChain の基礎                                            | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yoshidashingo/langchain-book/blob/main/chapter4/notebook.ipynb) |
| 第 5 章 LangChain の活用                                            | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yoshidashingo/langchain-book/blob/main/chapter5/notebook.ipynb) |
| 第 6 章 外部検索、履歴を踏まえた応答をする Web アプリの実装         | [完成するソースコードはこちら](./chapter6/)                                                                                                                                           |
| 第 7 章 ストリーム形式で履歴を踏まえた応答をする Slack アプリの実装 | [完成するソースコードはこちら](./chapter7/)                                                                                                                                           |
| 第 8 章 社内文書に答える Slack アプリの実装                         | [完成するソースコードはこちら](./chapter8/)                                                                                                                                           |
|                                                                     |

第 6 章から第 8 章の各節時点のソースコードは [details](./details) ディレクトリ以下を参照してください。

## 動作確認環境

本書のソースコードは以下の環境・バージョンで動作確認しました。

| 章               | 環境                        | Python  | LangChain |
| ---------------- | --------------------------- | ------- | --------- |
| 第 3 章〜第 5 章 | Google Colab                | 3.10.12 | 0.0.292   |
| 第 6 章〜第 8 章 | AWS Cloud9 (Amazon Linux 2) | 3.10.13 | 0.0.292   |

その他の Python パッケージの動作済みバージョンは、各章のディレクトリの requirements.txt (または requirements-dev.txt) を参照してください。

第 7 章・第 8 章のソースコードのデプロイに使用した Serverless Framework とそのプラグインは、以下のバージョンで動作確認しました。

- serverless@3.35.2
- serverless-python-requirements@6.0.0
- serverless-dotenv-plugin@6.0.0

## 書籍の誤り・エラーについて

書籍の誤り（誤字など）や、発生したエラーについては、GitHub の Issue からご連絡ください。

https://github.com/yoshidashingo/langchain-book/issues

## 正誤表

[正誤表](./errata.md)

## リンク

- [技術評論社](https://gihyo.jp/book/2023/978-4-297-13839-4)
- [Amazon.co.jp](https://www.amazon.co.jp/dp/4297138395)
