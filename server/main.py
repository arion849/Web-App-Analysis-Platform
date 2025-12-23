# API routes

from fastapi import FastAPI
from server import state

app = FastAPI(title = "Web Appilcation Analysis Platform")


@app.get("/health")
def health():
    return {"status" : "ok"}
