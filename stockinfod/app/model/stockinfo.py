import pandas as pd

def getStockInfo(productID, csvPath):
    try:
        df = pd.read_csv(csvPath)
        available_qty = df.loc[df["productID"] == productID, "available"].iloc[0]
        return int(available_qty)
    except:
        return -1