import requests, json

url = "https://marine-api.open-meteo.com/v1/marine?latitude=78&longitude=44&hourly=wave_height"
response = requests.get(url)
data = response.json()
print(data)

json = json.dumps(data, indent=4)
with open(r"C:\Users\ROYDEN\OneDrive\Desktop\phytelco\Day_22\scr2.json", "w") as file:
    file.write(json)