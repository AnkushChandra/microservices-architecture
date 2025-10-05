from model.stockinfo import getStockInfo
import os
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI

app= FastAPI()

csv="/code/app/model/stockinfo.csv"

@app.get("/")
def home():
    return {"health":"stock info ok"}

@app.get("/stock-info/items/{productID}")
def get_stock_info( productID : str ):
    stock = getStockInfo(productID,csv)
    if stock == -1:
        raise HTTPException(status_code=404, detail="Product not found")
    return { "productID": productID, "available": stock }
