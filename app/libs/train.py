import datetime
from pathlib import Path

import joblib
import yfinance as yf
from prophet import Prophet

BASE_DIR = Path(__file__).resolve(strict=True).parent


def train(ticker="MSFT"):
    TODAY = datetime.date.today()
    one_year_ago = datetime.datetime.now() - datetime.timedelta(days=365)
    
    try:
        data = yf.download(ticker, one_year_ago.strftime("%Y-%m-%d"), TODAY.strftime("%Y-%m-%d"))
        # print(data.head())
        # print(data.info())
        data["Adj Close"].plot(title=f"{ticker} Stock Adjusted Closing Price")

        df_forecast = data.copy()
        df_forecast.reset_index(inplace=True)
        df_forecast["ds"] = df_forecast["Date"]
        df_forecast["y"] = df_forecast["Adj Close"]
        df_forecast = df_forecast[["ds", "y"]]
        df_forecast
        # print(df_forecast.head())
        # print(' ')

        model = Prophet()
        model.fit(df_forecast)

        joblib.dump(model, Path(BASE_DIR).joinpath(f"trained_models/{ticker}.joblib"))

        return f"Model for {ticker} created/updated."
    except Exception as e:
        return f"Error happen - {e}"