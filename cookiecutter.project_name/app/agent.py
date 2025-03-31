import google.generativeai as genai
from app.config import GOOGLE_API_KEY

genai.configure(api_key=GOOGLE_API_KEY)

def ask_gemini(query: str):
    """Sends a query to Google Gemini AI and returns a response."""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(query)
    return response.text
