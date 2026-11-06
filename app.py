from fastapi import FastAPI

app = FastAPI(title="DevOps Health API", version="1.0.0")

@app.get("/")
def root():
    return {"message": "DevOps Health API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/version")
def version():
    return {"version": "1.0.0"}
