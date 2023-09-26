import logging
import os
import sys

import pinecone
from dotenv import load_dotenv
from langchain.document_loaders import UnstructuredPDFLoader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import Pinecone

load_dotenv()

logging.basicConfig(
    format="%(asctime)s [%(levelname)s] %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


def initialize_vectorstore():
    pinecone.init(
        api_key=os.environ["PINECONE_API_KEY"],
        environment=os.environ["PINECONE_ENV"],
    )

    index_name = os.environ["PINECONE_INDEX"]
    embeddings = OpenAIEmbeddings()
    return Pinecone.from_existing_index(index_name, embeddings)


if __name__ == "__main__":
    file_path = sys.argv[1]
    loader = UnstructuredPDFLoader(file_path)
    raw_docs = loader.load()
    logger.info("Loaded %d documents", len(raw_docs))

    text_splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    docs = text_splitter.split_documents(raw_docs)
    logger.info("Split %d documents", len(docs))

    vectorstore = initialize_vectorstore()
    vectorstore.add_documents(docs)
