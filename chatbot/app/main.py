from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="AI Chatbot API")

app.include_router(router)
