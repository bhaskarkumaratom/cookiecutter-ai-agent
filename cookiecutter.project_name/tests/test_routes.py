from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_ask_api():
    """Test /ask API endpoint."""
    response = client.post("/ask", json={"query": "Hello!"})
    assert response.status_code == 200
    assert "response" in response.json()

def test_search_api():
    """Test /search API endpoint."""
    response = client.post("/search", json={"query": "LangChain"})
    assert response.status_code == 200
    assert "results" in response.json()
