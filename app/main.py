from fastapi import FastAPI
from schemas.chat import ChatRequest, ChatResponse
from tutor.engine import tutor_response
from tutor.prompt import build_tutor_prompt, TEACHING_PROMPT, PRACTICE_TRANSITION_TEXT
from memory.service import get_student_memory, update_student_memory
from practice.question_generator import generate_question
from practice.question_evaluator import evaluate_subjective_answer
from practice.question_prompt import QUESTION_GENERATION_PROMPT
from tutor.state import TutorState
from rag.retriever import retrieve_context


app = FastAPI(title="Accounting Tutor Bot", version="1.0.0")
SESSION = TutorState(topic="Managing Ledgers")

@app.post("/health")
def health_check():
    return{'status': 'ok'}

@app.post("/chat")
def chat(request: ChatRequest):
    global SESSION, CURRENT_QUESTION

    if SESSION.mode == "teach":
        prompt = TEACHING_PROMPT.format(topic=SESSION.topic)
        response = tutor_response(prompt + "\nStudent says:\n" + request.message)

        SESSION.mark_explanation()

        if SESSION.ready_for_practice():
            SESSION.mode = "practice"
            response += "\n" + PRACTICE_TRANSITION_TEXT

        return {"response": response}

    if SESSION.mode == "practice":
        CURRENT_QUESTION = generate_question(
            topic=SESSION.topic,
            mastery=0.5
        )
        SESSION.mode = "evaluate"
        return CURRENT_QUESTION


@app.post("/practice/evaluate")
def evaluate_practice(payload: dict):
    global SESSION

    evaluation = evaluate_subjective_answer(
        question=payload["question"],
        student_answer=payload["student_answer"]
    )

    if evaluation["is_correct"]:
        SESSION.mode = "teach"
    else:
        SESSION.mode = "practice"

    return evaluation