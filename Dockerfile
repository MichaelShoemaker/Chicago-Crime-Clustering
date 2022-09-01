FROM python:3.8-slim-buster

WORKDIR /app

COPY requirements.txt ./scripts ./

RUN pip3 install -r requirements.txt