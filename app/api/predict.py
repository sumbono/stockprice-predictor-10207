from fastapi import APIRouter, HTTPException

from app.libs.convert import convert
from app.libs.models import StockOut
from app.libs.predict import predict
from app.workers import background_threads


predict_endpoint = APIRouter()

@predict_endpoint.post("/predict/{stock_name}", response_model=StockOut, status_code=200, tags=["predict"])
async def get_prediction(stock_name: str):
    ticker = stock_name.split('|')[0].strip()
    prediction_list = await background_threads.run(predict, ticker)
    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.\nTrain it first!")
    forecast = convert(prediction_list)
    response_object = {"ticker": ticker, "forecast": forecast}
    return response_object