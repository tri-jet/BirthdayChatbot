# BirthdayChatbot

A prototype chatbot application using the OpenAI API that reveals a secret letter to theuser. The user has to enter their birthday, which is saved in birthday.txt, to reveal thesecret letter which is in secret.txt.

## How to Install and Run
1. Clone the project
2. Create a python virtual environment using venv or conda
3. Install the dependencies using the `requirements.txt` file using the command: `pip install -r requirements.txt`
4. Create a file called `config.py` with the API information, with the following variables: LLM_API_KEY, ENDPOINT, DEPLOYMENT
 - e.g. `LLM_API_KEY = 'xyz', ENDPOINT = 'https://openai.com', DEPLOYMENT = 'gpt3'`

5. Run the main python script using `python main.py`

