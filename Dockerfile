FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

RUN apt-get update && apt-get install -y redis-server

COPY ./main.py /app/main.py

WORKDIR /app

EXPOSE 80
EXPOSE 6379

# Запускаем Redis и приложение
CMD service redis-server start && uvicorn main:app --host 0.0.0.0 --port 80