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
        {"role": "system", "content": "You are an assistant, deciphering the user's inputted date, which \
         may be in different languages, into a full date in English. If they are missing a part of the date e.g. day, month or year, tell \
         them what they are missing or where the date is in correct i.e. if they state a 13 month which doesn't exist."},
        {"role": "user", "content": "treinta de february 2008"}
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


