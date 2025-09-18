from fastapi import FastAPI

app = FastAPI(
    title="Metadata Management API",
    description="API for managing the corporate data infrastructure metadata.",
    version="0.1.0",
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Metadata Management API"}

@app.get("/api/v1/health")
def health_check():
    return {"status": "ok"}
