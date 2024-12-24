from fastapi import FastAPI
from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

celery = Celery(
    __name__,
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
)

@celery.task
def example_task(message: str):
    return f"Task completed with message: {message}"

from fastapi import FastAPI, UploadFile, File
from celery import Celery
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

celery = Celery(
    __name__,
    broker=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
    backend=os.getenv("REDIS_URL", "redis://localhost:6379/0"),
)

@celery.task
def example_task(message: str):
    return f"Task completed with message: {message}"

@app.get("/")
async def root():
    task = example_task.delay("Hello from Celery!")
    return {"message": "Hello from the backend!", "task_id": task.id}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename, "message": "File uploaded successfully"}
