import requests

# Endpoints
__words = "https://api.sheety.co/821149c0243c0b587c7d697954e3210c/trickyWords/trickywords"
__questions = "https://api.sheety.co/821149c0243c0b587c7d697954e3210c/trickyWords/questions"

# function to get the words information
def get_tricky_words():
    response = requests.get(__words)
    return response.json()["trickywords"]

def get_questions(word):
    response = requests.get(__questions)
    return response.json()["questions"]