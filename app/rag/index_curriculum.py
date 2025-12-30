import os
from pathlib import Path
from app.rag.chroma_store import collection
from app.rag.pdf_loader import load_pdf_text
from app.rag.chunker import chunk_text
from app.rag.embedder import embed_text

CURRICULUM_DIR = Path("curriculum")

if not CURRICULUM_DIR.exists():
    raise FileNotFoundError(f"Curriculum directory not found: {CURRICULUM_DIR}")

print(CURRICULUM_DIR)

for file_path in CURRICULUM_DIR.iterdir():
    if file_path.suffix == ".pdf":
        text = load_pdf_text(file_path)
        chunks = chunk_text(text)
        for i, chunk in enumerate(chunks):
            embeddings = embed_text(chunk)[0]
            embedding_vector = embeddings.values
            collection.add(
                documents=[chunk],
                metadatas=[{"source": file_path.name, "chunk_index": i}],
                ids=[f"{file_path.stem}_chunk_{i}"],
                embeddings=embedding_vector
            )

print("Curriculum indexed into ChromaDB successfully.")