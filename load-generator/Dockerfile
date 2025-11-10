FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV TARGET_URL=http://51.20.96.40:5000/apidocs/

CMD ["python", "generator.py"]
