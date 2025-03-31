from app.agent import ask_gemini

def test_ask_gemini():
    """Test that Gemini AI returns a non-empty response."""
    response = ask_gemini("What is AI?")
    assert isinstance(response, str)
    assert len(response) > 0
