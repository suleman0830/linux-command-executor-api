from fastapi import FastAPI
from routes.routes import router
import json

app = FastAPI()
app.include_router(router)

@app.get("/")
def health():
    return {"status": "Command Execution API is running"}

@app.get("/health")
def health():
    return {"status": "healthy"}