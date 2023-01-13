from dataclasses import dataclass
from DataModels.QuestionDataModel import QuestionDataModel

@dataclass
class WordDataModel:
    idTrickyWord: str
    trickyWord: str
    nBook: int
    nLesson: int
    difficulty: int
    questions: list[QuestionDataModel]
    type: int