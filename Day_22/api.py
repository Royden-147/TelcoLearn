import requests

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)
print("Response:",response.json())

post = requests.post(url, data = {
    "userId": 11,
    "id":101,
    "title":"foot",
    "body":"bar"
})
print("\nStatus Code:", post.status_code)
print("\nPost Response:",post.json())

# file = open("file.json")
# print(file.read())
