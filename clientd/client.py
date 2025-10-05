import requests
import json


url = "<url>/lookup"

# If Item Info = 200 and Stock = 200, return merged information.
payload = {"productID" : "XYZ-12345"}
response = requests.post(url, json.dumps(payload))
print("When: If Item Info = 200 and Stock = 200, return merged information.")
print(payload)
print(response.text+"\n")


# If Item Info = 404, return 404 to client. (No product.)
payload = {"productID" : "XYZ-12347"}
response = requests.post(url, json.dumps(payload))
print("When: If Item Info = 404, return 404 to client. (No product.)")
print(payload)
print(response.text+"\n")


# If Item Info = 200 and Stock = 404, return 200 with available: 0.

payload = {"productID" : "XYZ-12346"}
response = requests.post(url, json.dumps(payload))
print("When: If Item Info = 200 and Stock = 404, return 200 with available: 0.")
print(payload)
print(response.text+"\n")

