from fastapi import FastAPI

app = FastAPI(
    title="Decision X API",
    description="Cybersecurity Decision Support Platform",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Decision X backend is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }