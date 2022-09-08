import datetime
from pathlib import Path

import joblib
import yfinance as yf
from prophet import Prophet

BASE_DIR = Path(__file__).resolve(strict=True).parent
TODAY = datetime.date.today()


def train(ticker="MSFT"):
    try:
        data = yf.download(ticker, "2021-06-01", TODAY.strftime("%Y-%m-%d"))
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

        return f"Model for {ticker} created."
    except Exception as e:
        return f"Error happen - {e}"