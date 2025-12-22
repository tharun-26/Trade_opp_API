
from fastapi import FastAPI, Depends
from app.security import verify_token
from app.analyzer import analyze_sector

app = FastAPI(title="Trade Opportunities API")

@app.get("/analyze/{sector}")
async def analyze(sector: str, token: str = Depends(verify_token)):
    return await analyze_sector(sector)
