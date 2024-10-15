import requests

# Define the URL you want to send the request to
url = 'http://localhost:3000'

# Send a GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    print("Request was successful.")
    print("Response content:")
    print(response.text)  # Print the content of the response
else:
    print(f"Request failed with status code: {response.status_code}")
