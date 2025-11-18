from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import os
import openai

openai.api_key = os.getenv("OPENAI_API_KEY")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatReq(BaseModel):
    message: str

@app.post("/chat")
async def chat(req: ChatReq):
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role":"system","content":"You are Chat6GPT, a friendly multilingual assistant."},
                {"role":"user","content":req.message}
            ]
        )
        answer = resp["choices"][0]["message"]["content"]
        return {"reply": answer}
    except Exception as e:
        return {"error": str(e)}
