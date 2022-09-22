from fastapi import APIRouter, HTTPException

from app.libs.train import train
from app.workers import background_threads


train_endpoint = APIRouter()

# API endpoint
@train_endpoint.post("/train/{stock_name}", status_code=200, tags=["train"])
async def train_model(stock_name: str):
    ticker = stock_name.split('|')[0].strip()
    train_model_status = await background_threads.run(train, ticker)
    if not train_model_status:
        raise HTTPException(status_code=400, detail="Model could not being trained.")
    return {"training_result": train_model_status}
