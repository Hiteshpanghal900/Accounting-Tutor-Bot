from google import genai 
from pathlib import Path
from app.config import GEMINI_API_KEY
from .pdf_loader import load_pdf_text
from .chunker import chunk_text

client = genai.Client(api_key=GEMINI_API_KEY)

def embed_text(text: str):
    response = client.models.embed_content(
        model="gemini-embedding-001",
        contents = text
    )
    return response.embeddings
