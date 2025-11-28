import json

with open("wifi.json") as file:
    data = json.load(file)

print(data[0]["index"])