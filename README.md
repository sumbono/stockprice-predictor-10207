# StockPricesPredictor App 🚀
A demonstration of serving machine learning models with FastAPI.

## Pre-trained Stock Models
This is a stock's prices prediction app. input a stock name, then you will get forecast of the stock price for the next 7 days.

We already have some pre-trained stock models listed below.

```bash
| STOCK | COMPANY |
------------------------------
| AAPL | Apple Inc. |
| MSFT | Microsoft Corporation |
| GOOGL | Alphabet Inc. |
| GOOG | Alphabet Inc. |
| AMZN | Amazon.com, Inc. |
| TSLA | Tesla, Inc. |
| META | Meta Platforms, Inc. |
| NVDA | NVIDIA Corporation |
| KO | The Coca-Cola Company |
| VZ | Verizon Communications Inc. |
| AMD | Advanced Micro Devices, Inc. |
| INTC | Intel Corporation |
| NFLX | Netflix, Inc. |
| BYDDY | BYD Company Limited |
| ENB | Enbridge Inc. |
| OXY | Occidental Petroleum Corporation |
| PANW | Palo Alto Networks, Inc. |
| CRWD | CrowdStrike Holdings, Inc. |
| LNG | Cheniere Energy, Inc. |
| HPO | HP Inc. |
| SNAP | Snap Inc. |
| MDB | MongoDB, Inc. |
| BBY | Best Buy Co., Inc. |
| CHWY | Chewy, Inc. |
| FSLR | First Solar, Inc. |
| OKTA | Okta, Inc. |
| CHPT | ChargePoint Holdings, Inc. |
| EE | Excelerate Energy, Inc. |
| RKLB | Rocket Lab USA, Inc. |
| TELL | Tellurian Inc. |
```

## Live App
Check out the [Site](https://stockprice-predictor-10207.herokuapp.com/).

![](app/static/images/SPP_homepage.gif)


<!-- ## How To Use The Live App

- ### Predict: 
    ![](app/static/images/predict_stock_prices.gif)

- ### Train:
    ![](app/static/images/train_new_stock.gif) -->


## How To Start The App

- Clone this repository

```sh
$ git clone https://github.com/sumbono/stockprice-predictor-10207.git
$ cd stockprice_predictor
```

### With Docker

1. Build and tag the Docker image:

    ```sh
    $ docker build -t stock-price-app .
    ```

1. Spin up the container:

    ```sh
    $ docker run --name stock-price-app -e PORT=8008 -p 8008:8008 -d stock-price-app:latest
    ```

1. Test:

    ```sh
    $ curl \
      --header "Content-Type: application/json" \
      --request POST \
      http://localhost:8008/predict/MSFT
    ```

### Without Docker

1. Download and install poetry:
    - Using official installer:
        ```sh
        $ curl -sSL https://install.python-poetry.org | python -
        $ export PATH="$HOME/.local/bin:$PATH"
        ```
    - Using pip:
        ```sh
        $ pip install poetry
        ```
        or
        ```sh
        $ pip install poetry==1.1.15
        ```

1. Install the app dependencies using poetry:

    ```sh
    $ poetry install
    ```

1. Run the app:

    ```sh
    $ poetry run uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8008
    ```

1. Test:

    ```sh
    $ curl \
      --header "Content-Type: application/json" \
      --request POST \
      http://localhost:8008/predict/MSFT
    ```


## Credit

- gif file created using [ScreenToGif](https://www.screentogif.com/) 