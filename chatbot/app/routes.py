from fastapi import APIRouter, HTTPException
from app.schemas import ChatRequest, ChatResponse
from app.llm_service import generate_reply

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat_with_ai(data: ChatRequest):

    prompt = data.prompt.strip()

    if not prompt:
        raise HTTPException(status_code=400, detail="Prompt cannot be empty")

    try:
        reply = generate_reply(prompt)

        return {"reply": reply}

    except Exception:
        raise HTTPException(status_code=500, detail="AI service failed")
