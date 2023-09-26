import os

import pinecone
from dotenv import load_dotenv

load_dotenv()

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENV"],
)

index_name = os.environ["PINECONE_INDEX"]

if index_name in pinecone.list_indexes():
    pinecone.delete_index(index_name)

pinecone.create_index(name=index_name, metric="cosine", dimension=1536)
