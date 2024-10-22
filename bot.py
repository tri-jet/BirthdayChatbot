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

def input_birthday(user_input):
    data = {
        "messages": [
            {"role": "system", "content": "You are an assistant, deciphering the user's inputted date, which \
            may be in different languages, into a full date in English in the dd/mm/yyyy format. If they are missing a part of the date e.g. day, month or year, tell \
            them what they are missing or where the date is in correct i.e. if they state a 13 month which doesn't exist. Also if they enter a date in the future, give \
            them feedback that that date hasn't happened yet so it can't be their birthday. If the response is a valid date, respond with Y: <correct_date>\
            if the date may be different based on the format they use i.e. day, month year vs month,day, year, respond with A: and ask which they meant using the full word form to clarify \
            in the language they responded in, if the response is invalid, respond in the language they inputted in with N: <feedback>. With the response being English if no language is used. "},
            {"role": "user", "content": user_input}
        ], 
        "max_tokens": 50,
        "temperature": 0.5
    }

    response = requests.post(url, headers=headers,json=data)

    if response.status_code == 200:
        response = response.json()
        choices = response.get("choices")
        result = choices[0]['message']['content']
        #print(result)
        return result
    else:
        print(f"Error {response.status_code}: {response.text}")