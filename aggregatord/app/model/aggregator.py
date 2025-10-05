import requests


def getItemData(itemUrl,stockUrl,productID):

    try:
        r1 =requests.get(f"{itemUrl}/item-info/items/{productID}", verify=False)
    except:
        return -2,-2
    if r1.status_code==404:
        return -1,-1
    if r1.status_code != 200:
        return -2,-2
    item_data = r1.json()
    
    try:
        r2 =requests.get(f"{stockUrl}/stock-info/items/{productID}", verify=False)
    except:
        return -2,-2
    if r2.status_code==404:
        available = 0
    elif r2.status_code == 200:
        stock_data = r2.json()  
        available = int(stock_data.get("available", 0))
    else:
        return -2,-2
    
    return item_data["name"], available

