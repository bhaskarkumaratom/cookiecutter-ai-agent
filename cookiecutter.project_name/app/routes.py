from fastapi import FastAPI
from app.agent import ask_gemini
from app.search_tool import search_google

app = FastAPI(title="AI Search Agent")

@app.post("/ask")
def ask(query: str):
    """Asks Gemini AI a question."""
    return {"response": ask_gemini(query)}

@app.post("/search")
def search(query: str):
    """Searches Google and returns top results."""
    return {"results": search_google(query)}
