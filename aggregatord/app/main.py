from model.aggregator import getItemData
import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app= FastAPI()

ITEMINFO_URL = os.getenv("ITEMINFO_URL", "http://localhost:8088")
STOCKINFO_URL = os.getenv("STOCKINFO_URL", "http://localhost:8080")

class MessageIn(BaseModel):
    productID: str


@app.get("/")
def home():
    return {"health":"aggregator ok"}

@app.post("/lookup")
def get_stock_info( payload: MessageIn):
    name, available = getItemData(ITEMINFO_URL, STOCKINFO_URL, payload.productID)
    if name == -1 and available == -1:
        raise HTTPException(status_code=404, detail="Product not found")
    if name == -2 and available == -2:
        raise HTTPException(status_code=500, detail="Error with downstream microservices")
    return { "productID": payload.productID, "name": name, "available":available }

