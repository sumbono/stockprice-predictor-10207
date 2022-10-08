from fastapi import APIRouter, HTTPException

from app.api.stock_name import StockName
from app.libs.train import train


train_endpoint = APIRouter()

@train_endpoint.post("/train/{stock_name}", status_code=200, tags=["train"])
async def train_model(stock_name: StockName):
    train_model_status = train(stock_name)
    if not train_model_status:
        raise HTTPException(status_code=400, detail="Model could not being trained.")
    return {"training_result": train_model_status}
