import uuid
import requests
from DataModels.QuestionDataModel import QuestionDataModel
from DataModels.WordDataModel import WordDataModel

# Endpoints
__words = "https://api.sheety.co/821149c0243c0b587c7d697954e3210c/trickyWords/trickywords"
__questions = "https://api.sheety.co/821149c0243c0b587c7d697954e3210c/trickyWords/questions"

# function to get the words information
def get_tricky_words():
    response = requests.get(__words)
    new_list = []
    for item in response.json()["trickywords"]:
        new_item = WordDataModel(
            str(uuid.uuid4().hex),
            item["word"],
            item["nBook"],
            item["nlesson"],
            item["difficulty"],
            # get_questions(item["word"]),
            item["type"]
        )
        new_list.append(new_item)
    return new_list

def get_questions(word):
    response = requests.get(__questions)
    new_list = []

    for item in response.json()["questions"]:
        if item["word"] == word.lower():
            new_item = QuestionDataModel(
                item["question"],
                item["correctAnswer"],
                item["optionA"],
                item["optionB"],
                item["optionC"]
            )
            new_list.append(new_item)
    return new_list