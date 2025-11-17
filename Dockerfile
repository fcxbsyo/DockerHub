FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PORT=5010
EXPOSE 5010

CMD ["python", "app.py"]
