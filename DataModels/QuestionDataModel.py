from dataclasses import dataclass, asdict
from json import dumps

@dataclass
class QuestionDataModel:
    question: str
    correctAnswer: str
    optionA: str
    optionB: str
    optionC: str

    @property
    def __dict__(self):
        return asdict(self)

    @property
    def json(self):
        return dumps(self.__dict__)