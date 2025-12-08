import requests

# fdea6d5646535a4c4686098da93fd92 API key
res = requests.get("https://api.ipapi.com/api/check?access_key=fdea6d5646535a4c4686098da93fd92") 
data = res.json()
status = res.status_code
if(status == 200):
    print(data)
    print("Status code:", status)   
else:
    print("Error:", status) 