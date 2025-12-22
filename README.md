
# Trade Opportunities API

FastAPI service that analyzes Indian market sectors and returns AI-generated trade opportunity reports in Markdown format.

## Features
- FastAPI backend
- Google Gemini AI integration
- JWT Authentication
- Rate limiting
- In-memory storage
- Markdown report output

## Setup
```bash
pip install -r requirements.txt
export GEMINI_API_KEY=your_key
uvicorn app.main:app --reload
```

## Endpoint
GET /analyze/{sector}
