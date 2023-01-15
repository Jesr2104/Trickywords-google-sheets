import json
import uuid
import requests

# Endpoints
__words = "?action=getWords"
__questions = "?action=getQuestions"
__doc_validation = "AKfycbzSCON_JWG93S2kcrBk5f808pClMaYvUHhAx_TOE9wGeuk1de9ufkVM6L8idMsvPYFy"
__baseURL = "https://script.google.com/macros/s/"
__restURL = "/exec"


def get_words():
    tricky_words = get_tricky_words_dict()
    save_as_json(tricky_words)

    print("Number of items: ", len(tricky_words))
    print(tricky_words)


def save_as_json(tricky_words):
    with open('tricky_words.json', 'w') as f:
        json.dump(tricky_words, f)


# function to get the words information with dict
def get_tricky_words_dict():
    response_words = requests.get(__baseURL + __doc_validation + __restURL + __words)
    response_questions = requests.get(__baseURL + __doc_validation + __restURL + __questions)

    new_list_words = []
    for item in response_words.json():
        new_item = {
            "idTrickyWord": str(uuid.uuid4().hex),
            "trickyWord": item['word'],
            "nBook": item['nBook'],
            "nLesson": item['nLesson'],
            "difficulty": get_difficulty(item['difficult']),
            "questions": get_questions_dict(item['word'], response_questions),
            "type": get_type(item['type'])
        }

        if len(new_item["questions"]) > 0:
            new_list_words.append(new_item)
    return new_list_words


# function to ge the list of the questions with dict
def get_questions_dict(word, response_questions):
    new_list_questions = []

    for item in response_questions.json():
        if item['word'] == word.lower():
            new_item = {
                "question": item['question'],
                "correctAnswer": item['correctAnswer'],
                "optionA": item['optionA'],
                "optionB": item['optionB'],
                "optionC": item['optionC']
            }
            new_list_questions.append(new_item)
    return new_list_questions

def get_difficulty(difficulty_string):
    if difficulty_string.lower() == "easy".lower():
        return 1
    elif difficulty_string.lower() == "medium".lower():
        return 2
    elif difficulty_string.lower() == "hard".lower():
        return 3
    else:
        # without selection
        return 0

def get_type(type_string):
    if type_string.lower() == "Verbs".lower():
        return 1
    elif type_string.lower() == "Adjectives".lower():
        return 2
    elif type_string.lower() == "Nouns".lower():
        return 3
    elif type_string.lower() == "Phrasal verb".lower():
        return 4
    elif type_string.lower() == "Expression".lower():
        return 5
    else:
        return 0
