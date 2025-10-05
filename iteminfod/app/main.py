from model.iteminfo import getItemInfo
import os
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI

app= FastAPI()

csv="/code/app/model/iteminfo.csv"

@app.get("/")
def home():
    return {"health":"item info ok"}

@app.get("/item-info/items/{productID}")
def get_stock_info( productID : str ):
    stock = getItemInfo(productID,csv)
    if stock == -1:
        raise HTTPException(status_code=404, detail="Product not found")
    return { "productID": productID, "name": stock }

