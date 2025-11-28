import requests

def fetch_api_data(url):
    try:
        response = requests.get(url, timeout=5)

        # Check if the HTTP status code is ok (200–299)
        response.raise_for_status()

        # Try to parse JSON
        data = response.json()
        return data

    except requests.exceptions.Timeout:
        print("Error: The request timed out.")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except requests.exceptions.ConnectionError:
        print("Error: Unable to connect to the server.")
    except ValueError:
        print("Error: Response is not valid JSON.")
    except Exception as e:
        print(f"Unexpected error: {e}")
