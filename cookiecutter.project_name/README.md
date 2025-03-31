# Cookiecutter AI Agent

## Overview
This is a **Cookiecutter template** for building an **AI-powered agent** using **FastAPI, LangChain, LangGraph, and Google Gemini AI**. The template includes:
- **Google AI Studio (Gemini API)** for AI interactions
- **Google Search API** for real-world search results
- **FastAPI** for exposing the AI agent as an API
- **Unit, Integration & Smoke Tests**
- **CI/CD Automation** using GitHub Actions
- **Deployment to Google Cloud Run**

## Features
✅ **Pre-configured FastAPI server**  
✅ **Gemini AI integration for LLM responses**  
✅ **Google Search API for real-time web search**  
✅ **Automated unit, integration & smoke tests**  
✅ **CI/CD automation with GitHub Actions**  
✅ **Docker support for easy deployment**  
✅ **Cloud deployment via Google Cloud Run**  

---

## Project Structure
```
cookiecutter-ai-agent/
├── {{cookiecutter.project_name}}/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── agent.py        # Gemini AI logic
│   │   ├── search_tool.py  # Google Search API integration
│   │   ├── config.py       # API key management
│   │   ├── routes.py       # FastAPI endpoints
│   ├── tests/              # Test cases
│   │   ├── __init__.py
│   │   ├── test_agent.py   # Unit tests
│   │   ├── test_routes.py  # Integration tests
│   │   ├── test_smoke.py   # Smoke tests
│   ├── main.py             # FastAPI app entry point
│   ├── requirements.txt    # Dependencies
│   ├── Dockerfile          # Docker configuration
│   ├── .github/            # CI/CD automation
│   │   ├── workflows/
│   │   │   ├── ci.yml      # CI pipeline
│   │   │   ├── cd.yml      # Deployment pipeline
│   ├── README.md
├── cookiecutter.json
```

---

## Installation & Setup

### Prerequisites
- **Python 3.10+**
- **pip**
- **Git**
- **Docker (optional for deployment)**

### Install Cookiecutter
```bash
pip install cookiecutter
```

### Generate a New AI Agent Project
```bash
cookiecutter https://github.com/YOUR_GITHUB_USERNAME/cookiecutter-ai-agent
```
You will be prompted to enter:
- **Project Name**
- **API Keys (Gemini, Google Search, etc.)**

### Navigate to Your New Project
```bash
cd my_ai_agent
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run FastAPI Locally
```bash
uvicorn main:app --reload
```
API will be available at: `http://127.0.0.1:8000`

---

## Running Tests
### **Run All Tests**
```bash
pytest tests/
```

### **Run Specific Tests**
- **Unit Tests:**
  ```bash
  pytest tests/test_agent.py
  ```
- **Integration Tests:**
  ```bash
  pytest tests/test_routes.py
  ```
- **Smoke Tests:**
  ```bash
  pytest tests/test_smoke.py
  ```

---

## API Endpoints
### **Ask Gemini AI**
```http
POST /ask
```
#### **Request Body**
```json
{
  "query": "What is LangChain?"
}
```
#### **Response**
```json
{
  "response": "LangChain is a framework for LLM-based applications."
}
```

### **Search Google**
```http
POST /search
```
#### **Request Body**
```json
{
  "query": "Latest AI trends"
}
```
#### **Response**
```json
{
  "results": ["AI in 2025", "Top AI Tools"]
}
```

---

## CI/CD Automation
### **GitHub Actions Workflow**
#### **CI Pipeline (`ci.yml`)**
Runs **tests on every push**:
```yaml
name: CI - Run Tests

on:
  push:
    branches:
      - main
  pull_request:

tests:
  runs-on: ubuntu-latest
  steps:
    - name: Checkout Code
      uses: actions/checkout@v3
    - name: Install Dependencies
      run: |
        pip install -r requirements.txt
        pip install pytest
    - name: Run Tests
      run: pytest tests/
```

#### **CD Pipeline (`cd.yml`)**
Deploys to **Google Cloud Run**:
```yaml
name: CD - Deploy to Cloud Run

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v3
      - name: Authenticate with Google Cloud
        uses: google-github-actions/auth@v1
        with:
          credentials_json: ${{ secrets.GCP_SERVICE_ACCOUNT_KEY }}
      - name: Deploy
        run: |
          gcloud run deploy ai-agent --image gcr.io/${{ secrets.GCP_PROJECT_ID }}/ai-agent --platform managed --region us-central1 --allow-unauthenticated
```

---

## Deployment
### **Deploy Locally with Docker**
```bash
docker build -t ai-agent .
docker run -p 8000:8000 ai-agent
```

### **Deploy to Google Cloud Run**
```bash
gcloud run deploy ai-agent --image gcr.io/YOUR_PROJECT_ID/ai-agent --platform managed --region us-central1 --allow-unauthenticated
```

---

## Contributing
1. Fork the repository.
2. Create a new branch (`feature-new-feature`).
3. Commit your changes (`git commit -m "Added new feature"`).
4. Push to the branch (`git push origin feature-new-feature`).
5. Open a **Pull Request**.

---

## License
This project is licensed under the MIT License.

---

## Contact
For questions, reach out via [GitHub Issues](https://github.com/YOUR_GITHUB_USERNAME/cookiecutter-ai-agent/issues).

