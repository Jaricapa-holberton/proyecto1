from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"Message": "Hello World thanks to FastAPI"}