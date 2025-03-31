from langchain_community.tools import GoogleSearchRun
from app.config import SERPAPI_API_KEY

search_tool = GoogleSearchRun()

def search_google(query: str):
    """Performs a Google Search and returns results."""
    return search_tool.invoke(query)
