import chromadb
from chromadb.config import Settings

chroma_client = chromadb.PersistentClient(path="./chroma_db")

collection = chroma_client.get_or_create_collection(name="accounting_curriculum")