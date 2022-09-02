import datetime
from pathlib import Path

import joblib
import pandas as pd

BASE_DIR = Path(__file__).resolve(strict=True).parent
TODAY = datetime.date.today()


def predict(ticker="MSFT", days=7):
    model_file = Path(BASE_DIR).joinpath(f"trained_models/{ticker}.joblib")
    if not model_file.exists():
        return False

    model = joblib.load(model_file)

    future = TODAY + datetime.timedelta(days=days)

    dates = pd.date_range(start="2020-01-01", end=future.strftime("%m/%d/%Y"),)
    df = pd.DataFrame({"ds": dates})
    
    forecast = model.predict(df)

    # model.plot(forecast).savefig(f"{ticker}_plot.png")
    # model.plot_components(forecast).savefig(f"{ticker}_plot_components.png")

    return forecast.tail(days).to_dict("records")
