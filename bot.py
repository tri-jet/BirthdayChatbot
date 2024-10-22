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
            {"role": "system", "content": "You are an assistant that deciphers user inputted date, into a full English date format (Day Month Year) without ordinal suffixes.\
            You must handle input with various languages and ensuring accurate feedback.\
            1. if the date is valid and can't be confused with any other date in case of different formatting, respond with Y: <correct date>\
            2. if the date is missing the day, month, or year, tell them what's missing, responding with N: <your feedback> in the language they chose \
            3. if the date uses invalid dates e.g. non-existent months like 13, february with more than 28/29 days or a year in the future, respond \
               with N: <feedback on what makes the date invalid> in the language they chose \
            4. if the date uses invalid dates e.g. non-existent months like 13, but the date would be valid in different formats i.e. mm/dd/yy  \
               e.g. 6/13/2000 - would be valid as 13th june 2000, so respond with A: <clarification asking if they meant the valid date form of their input>\
            5. if the date in different formats e.g. dd/mm/yy and mm/dd/yy e.g. 5/6/2000 could be 5th June or 6th May,  respond with A: <clarification question, \
               asking which date they meant using the full word form for clarity in the language they chose\
             "},
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