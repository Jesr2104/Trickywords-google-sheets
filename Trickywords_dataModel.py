import dataclasses
from array import array


@dataclasses
class Questions:
    correctAnswer: str
    optionA: str
    optionB: str
    optionC: str
    question: str

@dataclasses
class WordDataModel:
    idTrickyWord: str
    trickyWord: str
    nBook: int
    nLesson: int
    difficulty: int
    questions: array[Questions]
    type: int
