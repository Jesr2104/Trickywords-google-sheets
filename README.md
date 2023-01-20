# Google Sheets Project

This project utilizes a Google Sheets document as a quick and efficient way to collect APIs and organize data. The data is separated by past book entries and formatted into JSON using Python, making it easy to insert into a database. This project also utilizes the real-time Firebase database to store the data.

**To set up this project, the following steps should be taken:**

- Create a Google Sheets document and make it accessible to users via a shared link or validation key (for added security, the document should be set to "reading mode" only).

- Create an Apps Script to allow the sheet to be accessed via an HTTP request.

- Deploy the service and use a Python script to query the data.

### The data format for this project is:

```
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
        
```

```
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
```

## What the project returns:

When executing the project, it returns a Json with all the list of objects that it extracts from Google Sheet and finishes completing its information in the python program.
