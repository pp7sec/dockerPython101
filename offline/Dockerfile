FROM python:3.9-slim

RUN adduser -D myuser
USER myuser

WORKDIR /app
COPY . /app

RUN pip install --user --upgrade pip
RUN pip install --user numpy
