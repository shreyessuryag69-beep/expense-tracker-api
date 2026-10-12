from fastapi import FastAPI
from . import models
from .database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Expense Tracker API", version="0.1.0")

@app.get("/health")
def health():
    return {"status": "ok"}