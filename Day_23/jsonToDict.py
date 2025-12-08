import json

with open("cars.json",'r') as crs:
    dict = json.load(crs)
print(dict)