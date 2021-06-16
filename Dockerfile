FROM python:3.8-slim-buster

RUN apt update && apt install make -y

WORKDIR /backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD gunicorn bbbs.wsgi:application --bind 0.0.0.0:8000