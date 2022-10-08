from pydantic import BaseModel
from typing import Dict


# pydantic models
class StockIn(BaseModel):
    ticker: str

class StockOut(StockIn):
    forecast: dict

class PredictionPlot(BaseModel):
    ticker: str
    forecast: Dict