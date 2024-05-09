import requests
import json

# Set up your Olmanna API endpoint
OLMANN_API_ENDPOINT = 'http://localhost:11434/api/generate'

# Create a dictionary to represent the JSON data
data = {
    "model": "llama3",
    "prompt": "Why is the sky blue?"
}

# Convert the dictionary to JSON format
json_data = json.dumps(data)

try:
    # Send the POST request with the JSON data
    response = requests.post(OLMANN_API_ENDPOINT, json=json_data)

    if response.status_code == 200:
        # Try parsing the JSON response as a string
        output_text = response.text
    else:
        # Handle any errors that might occur
        print(f"Error {response.status_code}: {response.reason}")
except requests.exceptions.RequestException as e:
    raise OlmannaAPIError(f"An error occurred: {e}")