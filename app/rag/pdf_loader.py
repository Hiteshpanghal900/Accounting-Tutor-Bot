from pypdf import PdfReader
from pathlib import Path

def load_pdf_text(file_path: str) -> str:
    reader = PdfReader(file_path)
    text = ""

    print(f"Total pages: {len(reader.pages)}")

    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text
