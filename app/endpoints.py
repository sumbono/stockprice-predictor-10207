from fastapi import FastAPI, HTTPException

from app.libs.convert import convert
from app.libs.models import StockOut
from app.libs.predict import predict
from app.libs.stock_name import StockName
from app.metadata import metadata
from app.workers import background_threads

app = FastAPI(
    title=metadata["title"],
    description=metadata["description"],
    version=metadata["version"],
    contact=metadata["contact"],
    openapi_tags=metadata["tags"]
)

@app.post("/predict/{stock_name}", response_model=StockOut, status_code=200, tags=["predict"])
async def get_prediction(stock_name: StockName):
    ticker = stock_name.split('|')[0].strip()
    prediction_list = await background_threads.run(predict, ticker)
    if not prediction_list:
        raise HTTPException(status_code=400, detail="Model not found.")
    forecast = await background_threads.run(convert, prediction_list)
    response_object = {"ticker": ticker, "forecast": forecast}
    return response_object