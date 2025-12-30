from rag.embedder import embed_text
from rag.chroma_store import collection

def retrieve_context(query: str, top_k: int = 3):
    query_embedding = embed_text(query)[0]
    embed_vector = query_embedding.values

    results = collection.query(
        query_embeddings=embed_vector,
        n_results=top_k
    )

    return results
