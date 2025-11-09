FROM python:3.10-slim

WORKDIR /app
COPY generator.py .
COPY requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "generator.py"]
