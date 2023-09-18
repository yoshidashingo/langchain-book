# ChatGPT、LangChain によるチャットシステム構築［実践］入門

「ChatGPT、LangChain によるチャットシステム構築［実践］入門」の GitHub リポジトリです。

https://www.amazon.co.jp/dp/4297138395

## 各章のソースコード

| 章                                        | Colab                                                                                                                                                                           |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 第 3 章 ChatGPT を API から利用するために | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yoshidashingo/langchain-book/blob/main/03/notebook.ipynb) |
| 第 4 章 LangChain の基礎                  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yoshidashingo/langchain-book/blob/main/04/notebook.ipynb) |
| 第 5 章 LangChain の活用                  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/yoshidashingo/langchain-book/blob/main/05/notebook.ipynb) |

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
