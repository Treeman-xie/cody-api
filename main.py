# main.py

from fastapi import FastAPI
from pydantic import BaseModel
from generator import generate_code

app = FastAPI()

class CodeRequest(BaseModel):
    prompt: str

@app.post("/generate")
async def generate_code_endpoint(request: CodeRequest):
    code = generate_code(request.prompt)
    return {"code": code}

@app.get("/")
async def root():
    return {"message": "Welcome to Cody - Your AI Coding Assistant!"}
