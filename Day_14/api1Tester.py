from api1Module import fetch_api_data

good_url = "https://jsonplaceholder.typicode.com/posts/1"
# bad_url  = "https://jsonplaceholder.typicode.com/invalidendpoint123"
# bad_url  = "https://jsonplaceholder"
# bad_url  = "https://thisdomaindoesnotexist123456789.com"
bad_url  = "https://httpstat.us/200?sleep=10000"  # Valid URL but will simulate non-JSON response for testing

# print("Testing GOOD URL:")
# print(fetch_api_data(good_url))

print("\nTesting BAD URL:")
print(fetch_api_data(bad_url))
