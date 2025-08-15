FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install cryptography

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir cryptography

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
