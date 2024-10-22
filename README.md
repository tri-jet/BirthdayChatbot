# BirthdayChatbot

A prototype chatbot application using the OpenAI API that reveals a secret letter to the user. The user has to enter their birthday, which is saved in birthday.txt, to reveal the secret letter which is in secret.txt.

## How to Install and Run
1. Clone the project
2. Create a python virtual environment using venv or conda
3. Install the dependencies in the `requirements.txt` file using the command: `pip install -r requirements.txt`
4. Create a file called `config.py` with the API information, with the following variables: LLM_API_KEY, ENDPOINT, DEPLOYMENT
 - e.g. `LLM_API_KEY = 'xyz', ENDPOINT = 'https://openai.com', DEPLOYMENT = 'gpt3'`

5. Run the main python script using `python main.py`, enter the right birthday and you'll see the secret message.

### How the Bot Script Works
The bot script deciphers user input to parse a valid date. 
The bot uses the following response tags to indicate whether it was able to parse a valid date from the input.
- Y (Yes) - valid date, proceed to check if date matches birthday.txt 
- N (No) - invalid date, provide feedback
- A(Ambiguous) - date can be interpreted differently in different formats, e.g. 5/6/2000 could be 5th June or 6th May.

## Testing
To run the tests, use the command `python -m unittest tests\test_bot.py` 

