# api2Tester_fixed.py
import requests
from api2Module import APIError   # your custom exception module

def fetch_api(url):
    try:
        response = requests.get(url, timeout=2)
        response.raise_for_status()
        try:
            return response.json()
        except ValueError:
            raise APIError("Response is not valid JSON")
    except requests.exceptions.Timeout:
        raise APIError("Request timed out")
    except requests.exceptions.ConnectionError:
        raise APIError("Host is unreachable")
    except requests.exceptions.HTTPError as e:
        raise APIError(f"HTTP Error: {e}")
    except Exception as e:
        raise APIError(f"Unexpected Error: {e}")

# <-- Ensure this list has exactly the 5 URLs (no duplicates) -->
test_urls = [
    "https://jsonplaceholder.typicode.com/posts/1",      # good
    "https://jsonplaceholder.typicode.com/unknownendpoint",  # 404
    "https://httpstat.us/200?sleep=10000",                # timeout (if timeout < 10s)
    "https://example.com",                                # non-JSON
    "https://thisdomaindoesnotexist123456789.com",         # host unreachable
    "https://httpstat.us/200?sleep=5000"
]

for url in test_urls:
    try:
        result = fetch_api(url)
        print(f"SUCCESS: {result}")
    except APIError as err:
        print(f"ERROR: {err}")
