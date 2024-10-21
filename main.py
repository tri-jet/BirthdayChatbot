import json

import requests

from config import LLM_API_KEY, ENDPOINT, DEPLOYMENT

api_key = LLM_API_KEY
endpoint = ENDPOINT
deployment = DEPLOYMENT

url = f'{endpoint}openai/deployments/{deployment}/chat/completions?api-version=2023-05-15'

headers = {
    'Content-Type':'application/json',
    'api-key':api_key
}

data = {
    "messages": [
        {"role": "system", "content": "You are an assistant, deciphering the user's inputted date, which may be in different languages, into English"},
        {"role": "user", "content": "Uno de enero 2007"}
    ], 
    "max_tokens": 50,
    "temperature": 0.5
}


response = requests.post(url, headers=headers,json=data)

if response.status_code == 200:
    result = response.json()
    print(json.dumps(result, indent = 2))
else:
    print(f"Error {response.status_code}: {response.text}")


