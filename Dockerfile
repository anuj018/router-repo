FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY milvus_sharding_router.py .
COPY milvus_router_client.py .
COPY run_router.py .

EXPOSE 8000

CMD ["python", "run_router.py"]
