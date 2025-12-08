import requests, json

url = "https://marine-api.open-meteo.com/v1/marine?latitude=13.3347&longitude=74.7462&hourly=wave_height"

response = requests.get(url)
data = response.json()

json = json.dumps(data, indent=4)
with open(r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\Day_22\scr1.json", "w") as file:
    file.write(json)