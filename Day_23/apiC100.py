import requests,json
url = "https://api.nationalize.io/?name=royden"

for i in range(1,105):
    res=requests.get(url)
    print(res)
    print(f"{i}- iteration")