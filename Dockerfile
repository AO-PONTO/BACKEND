FROM python:3.11-buster

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . app/

WORKDIR /app

EXPOSE 8000
