FROM python:3.9-slim

WORKDIR /app

# Install build tools and libswisseph dependencies
RUN apt-get update && \
    apt-get install -y gcc build-essential libffi-dev python3-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "app.py"]