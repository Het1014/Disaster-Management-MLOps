FROM python:3.11-slim

WORKDIR /app

# Copy requirements first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy ML code and model
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
