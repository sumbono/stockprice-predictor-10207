from fastapi import APIRouter, HTTPException

from app.api.stock_name import StockName
from app.libs.convert import convert
from app.libs.models import StockOut
from app.libs.predict import predict


predict_endpoint = APIRouter()

@predict_endpoint.post("/predict/{stock_name}", response_model=StockOut, status_code=200, tags=["predict"])
async def get_prediction(stock_name: StockName):
    prediction_list = predict(stock_name)
    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.\nTrain it first!")
    forecast = convert(prediction_list)
    response_object = {"ticker": stock_name, "forecast": forecast}
    return response_object