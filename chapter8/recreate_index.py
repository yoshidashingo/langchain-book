import os

from dotenv import load_dotenv
from pinecone import Pinecone, PodSpec

load_dotenv()

pc = Pinecone()

index_name = os.environ["PINECONE_INDEX"]

if index_name in pc.list_indexes().names():
    pc.delete_index(index_name)

pc.create_index(
    name=index_name,
    metric="cosine",
    dimension=1536,
    spec=PodSpec(environment=os.environ["PINECONE_ENV"]),
)
