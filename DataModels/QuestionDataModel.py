from dataclasses import dataclass

@dataclass
class QuestionDataModel:
    question: str
    correctAnswer: str
    optionA: str
    optionB: str
    optionC: str