import requests
import json

# Set up API key and endpoint URL
API_KEY = "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"
ENDPOINT_URL = "https://api.openai.com/v1/engines/davinci-codex/completions"

# Prompt user for input text
input_text = input("Enter text to summarize: ")

# Define request headers and parameters
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
}
data = {
    "prompt": "Take the story, and generate an AI art piece that would best reflect the themes, colors, characters, and abstract ideas laid out in the story itself. Here is the story: '\n{input_text}'",
    "max_tokens": 10,
    "temperature": 0.01
}

# Send API request and get response
response = requests.post(ENDPOINT_URL, headers=headers, json=data)

# Parse response and extract generated text
if response.status_code == 200:
    response_json = response.json()
    generated_text = response_json["choices"][0]["text"]
    print(generated_text)
else:
    print("Error: API request failed")
