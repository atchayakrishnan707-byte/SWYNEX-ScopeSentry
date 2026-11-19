
from fastapi import FastAPI

app = FastAPI(
    title="ScopeSentry API",
    description="AI-Powered Project Scope Management and Change Intelligence Platform",
    version="1.0.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to ScopeSentry API",
        "status": "Running"
    }

@app.get("/api/health")
def health_check():
    return {
        "application": "ScopeSentry",
        "status": "Healthy"
    }
