import uvicorn
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(
        "milvus_sharding_router:app", 
        host="0.0.0.0",
        port=port,
        workers=16,
        access_log=False,
        log_level="warning"
    )