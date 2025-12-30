from fastapi import FastAPI
from schemas.chat import ChatRequest, ChatResponse
from tutor.engine import tutor_response
from tutor.prompt import TUTOR_SYSTEM_PROMPT
from rag.retriever import retrieve_context


app = FastAPI(title="Accounting Tutor Bot", version="1.0.0")

@app.post("/health")
def health_check():
    return{'status': 'ok'}

@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    context = retrieve_context(request.message)

    full_prompt = f"""{TUTOR_SYSTEM_PROMPT}
        Context: {context}
        Student says: {request.message}
    """
    response = tutor_response(full_prompt)
    return ChatResponse(response=response)
