import pandas as pd

def getItemInfo(productID, csvPath):
    try:
        df = pd.read_csv(csvPath)
        item_info = df.loc[df["productID"] == productID, "name"].iloc[0]
        return item_info
    except:
        return -1