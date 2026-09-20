import json
class QuizQuestion:
    def __init__(self, title, question, answer):
        self.title = title
        self.question = question
        self.answer = answer

    def to_dic(self) -> dict:
        """Convert this object into a plain, safe for json.jump()."""
        return {"title": self.title, "question": self.question, "answer": self.answer}

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild a QuizzQuestion object from a plain dic (e.g. loaded from JSON)."""
        return cls(title=data["title"], question=data["question"], answer=data["answer"])


class StudySession:

    def __init__(self, title, summary, questions):
        self.title = title
        self.summary = summary
        self.questions = QuizQuestion

    def to_dic(self) -> dict:
        return {"title":self.title, "summary":self.summary, "questions":json.dumps(self.questions)}

    @classmethod
    def from_dict(cls, data: dict):
        return cls(title=data["title"], summary=data["summary"], questions = data["questions"])


num1 = QuizQuestion("variable", "is snakecase one of the way of declaring a variable", "True")
num2 = QuizQuestion("class", "class name is declared using camelcase", "True")

print(num1.to_dic())
print(num2.to_dic())

new_session = StudySession.from_dict(num1.to_dic)
# session2 = StudySession.from_dict(num2.to_dic)

print(new_session.questions[0].question)





