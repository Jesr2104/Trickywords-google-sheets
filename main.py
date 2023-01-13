# Trickywords google sheets APIs
from functions import get_tricky_words
from functions import get_questions

if __name__ == '__main__':
    # print(get_tricky_words())
    for item in get_questions("race"):
        print(item)