# StockPricesPredictor App
A demonstration of deploying and hosting a Machine Learning Model with FastAPI and Heroku.

## Live app

Check out the [site](https://stockprice-predictor-10207.herokuapp.com/docs).

## Want to use this project?

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

1. Train the model:

    ```sh
    $ docker exec -it stock-price-app python

    >>> from app.libs.train import train
    >>> train()
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

    ```sh
    $ curl -sSL https://install.python-poetry.org | python -
    $ export PATH="$HOME/.local/bin:$PATH"
    ```

1. Install the app dependencies using poetry:

    ```sh
    $ poetry install
    ```

1. Train the model:

    ```sh
    $ poetry run python

    >>> from app.libs.train import train
    >>> train()
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
