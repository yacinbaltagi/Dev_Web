class Question:
    def __init__(self, id=None, position=None, title=None, text=None, image=None, possibleAnswers=None):
        self.id = id
        self.position = position
        self.title = title
        self.text = text
        self.image = image
        self.possibleAnswers = possibleAnswers if possibleAnswers is not None else []

    def to_dict(self):
        return {
            'id': self.id,
            'position': self.position,
            'title': self.title,
            'text': self.text,
            'image': self.image,
            'possibleAnswers': [answer.to_dict() for answer in self.possibleAnswers]
        }

    @staticmethod
    def from_dict(data):
        possibleAnswers = [Answer.from_dict(ans) for ans in data.get('possibleAnswers', [])]
        return Question(
            id=data.get('id'),
            position=data.get('position'),
            title=data.get('title'),
            text=data.get('text'),
            image=data.get('image'),
            possibleAnswers=possibleAnswers
        )

class Answer:
    def __init__(self, id=None, question_id=None, text=None, isCorrect=None):
        self.id = id
        self.question_id = question_id
        self.text = text
        self.isCorrect = isCorrect

    def to_dict(self):
        return {
            'id': self.id,
            'question_id': self.question_id,
            'text': self.text,
            'isCorrect': self.isCorrect
        }

    @staticmethod
    def from_dict(data):
        return Answer(
            id=data.get('id'),
            question_id=data.get('question_id'),
            text=data.get('text'),
            isCorrect=data.get('isCorrect')
        )
