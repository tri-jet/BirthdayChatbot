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
         may be in different languages, into a full date in English in the dd/mm/yyyy format. If they are missing a part of the date e.g. day, month or year, tell \
         them what they are missing or where the date is in correct i.e. if they state a 13 month which doesn't exist. Also if they enter a date in the future, give \
         them feedback that that date hasn't happened yet so it can't be their birthday. If the response is a valid date, respond with YES: <correct_date>\
         if the response is invalid, respond in the language they inputted in with NO: <feedback> "},
        {"role": "user", "content": "treinta de february 2024"}
    ], 
    "max_tokens": 50,
    "temperature": 0.5
}


response = requests.post(url, headers=headers,json=data)

if response.status_code == 200:
    result = response.json()
    choices = result.get("choices")
    print(choices[0]['message']['content'])
else:
    print(f"Error {response.status_code}: {response.text}")