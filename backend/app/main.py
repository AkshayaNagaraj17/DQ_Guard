from fastapi import FastAPI
from app.api.upload import router as upload_router

app = FastAPI(
    title="DQGuard API",
    description="Data Quality and Duplicate Detection Platform",
    version="1.0.0"
)

app.include_router(
    upload_router,
    prefix="/api"
)


@app.get("/")
def root():
    return {
        "message": "Welcome to DQGuard API",
        "status": "running"
    }