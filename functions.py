import uuid
import requests
from DataModels.QuestionDataModel import QuestionDataModel
from DataModels.WordDataModel import WordDataModel

# Endpoints
__words = "?action=getWords"
__questions = "?action=getQuestions"
__doc_validation = "AKfycbzSCON_JWG93S2kcrBk5f808pClMaYvUHhAx_TOE9wGeuk1de9ufkVM6L8idMsvPYFy"
__baseURL = "https://script.google.com/macros/s/"
__restURL = "/exec"


def get_words_json():
    print(get_tricky_words())

# function to get the words information
def get_tricky_words():
    response_words = requests.get(__baseURL + __doc_validation + __restURL + __words)
    response_questions = requests.get(__baseURL + __doc_validation + __restURL + __questions)

    new_list_words = []
    for item in response_words.json():
        new_item = WordDataModel(
            str(uuid.uuid4().hex),
            item['word'],
            item['nBook'],
            item['nLesson'],
            item['difficult'],
            get_questions(item['word'], response_questions),
            item['type']
        )
        new_list_words.append(new_item.json)
    return new_list_words


# function to ge the list of the questions
def get_questions(word, response_questions):
    new_list_questions = []

    for item in response_questions.json():
        if item['word'] == word.lower():
            new_item = QuestionDataModel(
                item['question'],
                item['correctAnswer'],
                item['optionA'],
                item['optionB'],
                item['optionC']
            )
            new_list_questions.append(new_item)
    return new_list_questions
