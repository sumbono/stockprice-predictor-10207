import base64, json

from fastapi import APIRouter, HTTPException
from io import BytesIO
from matplotlib.figure import Figure
from pydantic import BaseModel
from typing import Dict

from app.api.stock_name import stock_name_dict

class StockPrediction(BaseModel):
    ticker: str
    forecast: Dict

predict_plotter_endpoint = APIRouter()

@predict_plotter_endpoint.post("/predict_plotter", status_code=200, tags=["predict_plotter"])
async def get_prediction_plot(stock_prediction: StockPrediction):
    print(stock_prediction.ticker)
    print(stock_prediction.forecast)
    
    dates = list(stock_prediction.forecast.keys())
    values = list(stock_prediction.forecast.values())

    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(6.4,5.4))
    ax = fig.subplots()
    ax.plot(dates, values)
    ax.tick_params(axis='x', rotation=30)
    ax.set_title(f"Prediction of {stock_name_dict[stock_prediction.ticker]} (in USD)")
    
    # Save it to a temporary buffer.
    buf = BytesIO()
    fig.savefig(buf, format="png")

    # Embed the result in the html output.
    data = base64.b64encode(buf.getbuffer()).decode("ascii")
    return json.dumps(f"<img id='gif_img' alt='center' src='data:image/png;base64,{data}'/>")