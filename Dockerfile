FROM python:3.9.6-slim-buster
LABEL maintainer="Sumbono <sumbono102@gmail.com>"

RUN apt-get -y update && apt-get install -y \
    apt-utils \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN echo $USER
RUN mkdir /opt/stockprice_predictor
WORKDIR /opt/stockprice_predictor
RUN ls
COPY . .
RUN ls -lh /opt/stockprice_predictor

RUN pip install --upgrade setuptools
RUN pip install pystan==3.5.0

RUN pip install -r requirements.txt

CMD gunicorn -w 3 -k uvicorn.workers.UvicornWorker app.main:app --bind 0.0.0.0:$PORT
