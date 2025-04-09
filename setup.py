from setuptools import setup, find_packages

setup(
    name="milvus-router",
    version="0.1.0",
    description="Milvus Sharding Router Server",
    packages=find_packages(),
    install_requires=[
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0", 
        "httpx>=0.20.0",
        "pymilvus>=2.0.0",
        "redis>=4.0.0",
        "numpy>=1.20.0",
        "pydantic>=1.8.0",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "milvus-router=milvus_sharding_router:start_server",
        ],
    },
)
