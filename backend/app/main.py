# contains entry point for the FastAPI application
from fastapi import FastAPI
from app.api import router as api_router

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Footy Dashboard API is running!"}

app.include_router(api_router)
