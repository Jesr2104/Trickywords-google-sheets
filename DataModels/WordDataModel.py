from json import dumps
from dataclasses import dataclass, asdict
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

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)