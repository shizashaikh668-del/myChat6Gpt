from fastapi import FastAPI
from pydantic import BaseModel
import os
from openai import OpenAI

app = FastAPI()

# Get API key from environment variable
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class Message(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "Chat6GPT is running successfully!"}

@app.post("/chat")
def chat(msg: Message):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": msg.text}]
        )

        reply = response.choices[0].message.content
        return {"answer": reply}

    except Exception as e:
        return {"error": str(e)}
