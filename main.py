from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import os
import openai

app = FastAPI()

# CORS Setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://shizashaikh668-del.github.io",
        "https://mychat6gpt.onrender.com",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

openai.api_key = os.getenv("OPENAI_API_KEY")

@app.get("/")
def home():
    return {"message": "ChatGPT backend is running!"}

# 🚀 Chat POST API
@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_msg = data.get("message")

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": user_msg}
            ]
        )

        bot_reply = response["choices"][0]["message"]["content"]
        return {"reply": bot_reply}

    except Exception as e:
        return {"error": str(e)}
