from .firestore_client import db
from .memory_schema import student_memory

COLLECTION_NAME = "student_memory"

def get_student_memory(student_id: str):
    """Retrieve the student's memory document. If it doesn't exist, create a new one."""
    doc_ref = db.collection(COLLECTION_NAME).document(student_id)
    doc = doc_ref.get()

    if doc.exists:
        return doc.to_dict()
    
    memory = student_memory(student_id)
    doc_ref.set(memory)
    return memory

def update_student_memory(student_id: str, updates: dict):
    """Update specific fields in the student's memory document."""
    doc_ref = db.collection(COLLECTION_NAME).document(student_id)
    doc_ref.update(updates)