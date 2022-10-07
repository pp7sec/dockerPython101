FROM python:3.9-slim

WORKDIR /app
COPY . /app

RUN pip install --root-user-action=ignore
RUN pip install --upgrade pip
RUN pip install numpy
