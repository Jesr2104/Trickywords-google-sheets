from array import array
from dataclasses import dataclass
from DataModels import QuestionDataModel

@dataclass
class WordDataModel:
    idTrickyWord: str
    trickyWord: str
    nBook: int
    nLesson: int
    difficulty: int
    questions: array[QuestionDataModel]
    type: int