# main.py
import os
from fastapi import FastAPI
from pydantic import BaseModel
import openai
from fastapi.middleware.cors import CORSMiddleware

openai.api_key = os.getenv("OPENAI_API_KEY")  # set this in Render env vars

app = FastAPI()

# Allow requests from your GitHub Pages origin and Render domain (adjust if needed)
origins = [
    "https://shizashaikh668-del.github.io",
    "https://mychat6gpt.onrender.com",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,    # restrict to your domains for safety
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    prompt: str

@app.get("/")
async def root():
    return {"message": "Chat6GPT backend: running"}

@app.post("/chat")
async def chat(req: ChatRequest):
    try:
        # Using ChatCompletion (gpt-3.5-turbo) - reliable choice
        resp = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role":"user","content": req.prompt}],
            max_tokens=500,
            temperature=0.7,
        )
        text = resp.choices[0].message.get("content", "").strip()
        return {"reply": text}
    except Exception as e:
        return {"error": str(e)}
