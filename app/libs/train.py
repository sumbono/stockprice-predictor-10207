import joblib
import yfinance as yf

from datetime import datetime, timedelta
from pathlib import Path
from prophet import Prophet

BASE_DIR = Path(__file__).resolve(strict=True).parent


def train(ticker="MSFT"):
    TODAY = datetime.today()
    n_year_ago = TODAY - timedelta(days=365*1)
    
    try:
        data = yf.download(ticker, n_year_ago.strftime("%Y-%m-%d"), TODAY.strftime("%Y-%m-%d"))
        data["Adj Close"].plot(title=f"{ticker} Stock Adjusted Closing Price")

        df_forecast = data.copy()
        df_forecast.reset_index(inplace=True)
        df_forecast["ds"] = df_forecast["Date"]
        df_forecast["y"] = df_forecast["Adj Close"]
        df_forecast = df_forecast[["ds", "y"]]
        df_forecast
        
        model = Prophet()
        model.fit(df_forecast)

        joblib.dump(model, Path(BASE_DIR).joinpath(f"trained_models/{ticker}.joblib"))

        return f"{ticker} model trained. \nStart to predict!"
    except Exception as e:
        return f"Error happen - {e}"