FROM python:3.9.6-slim-buster
LABEL maintainer="Sumbono <sumbono102@gmail.com>"

RUN apt-get update && apt-get install -y --no-install-recommends apt-utils gcc netcat net-tools curl
RUN useradd --create-home -u 1000 app

RUN mkdir /home/app/stockprice_predictor
WORKDIR /home/app/stockprice_predictor

RUN ls
COPY . .
RUN ls -a /home/app/stockprice_predictor

RUN chown app:app -Rf /home/app/
RUN ls -lh /home/app/stockprice_predictor

USER app

RUN curl -sSL https://install.python-poetry.org | python -
ENV PATH="/home/app/.local/bin:$PATH"
RUN poetry -V
RUN poetry install

# CMD poetry run gunicorn -w 3 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:$PORT
CMD poetry run uvicorn app.main:app --host 0.0.0.0 --port $PORT --workers 1 --timeout-keep-alive 30