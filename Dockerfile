FROM python:3.10

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .

EXPOSE 8080

CMD gunicorn --bind :8080 --log-level info app:server