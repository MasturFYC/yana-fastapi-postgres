FROM python:3.9

WORKDIR /app

COPY requirements.txt /app

RUN pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /app/src
COPY app.py /app

EXPOSE 8000

CMD ["uvicorn", "app:app", "--proxy-headers", "--host=0.0.0.0", "--reload"]

