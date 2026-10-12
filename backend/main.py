
from fastapi import FastAPI

app = FastAPI(title="RTPM-AIAlert API")


@app.get("/")
def home():
    return {
        "success": True,
        "data": {
            "project": "RTPM-AIAlert",
            "status": "running"
        },
        "message": "Backend is running successfully"
    }
