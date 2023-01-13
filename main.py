# Trickywords google sheets APIs
from functions import get_tricky_words

if __name__ == '__main__':
    for item in get_tricky_words():
        print(item)