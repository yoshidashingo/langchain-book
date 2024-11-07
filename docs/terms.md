# Terms

- Fine tuning
  既存のモデルに追加の学習をさせる

- In-context Learning (ICL)
  few-show prompting のように、prompt ないのいくつかの例によって言語 model に task を学ばせること

- LangChain
  LLM を使った Application 開発 framework です。LLM を使ったさまざまな種類の application で使うことができます。

- Hallucination
  LLM による想像の回答になること

- RAG(Retrieval Augmented Generation)
  文書を OpenAI の Embeddings API などで vector 化しておいて、入力 vector が違い文書を検索して context に含める手法を RAG と呼ぶ

  LangChain の Data connection では、とくに Vector store を使い、文書をベクトル化して保存しておいて、入力のテキストとベクトルの近い文書を検索して context に含めて使う方法が提供されています。

- Retriever
  text に関連する document を得る interface
