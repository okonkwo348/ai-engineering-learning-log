import json
class QuizQuestion:
    def __init__(self, title, question, answer):
        self.title = title
        self.question = question
        self.answer = answer

    def to_dict(self) -> dict:
        """Convert this object into a plain, safe for json.jump()."""
        return {"title": self.title, "question": self.question, "answer": self.answer}

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild a QuizzQuestion object from a plain dic (e.g. loaded from JSON)."""
        return cls(title=data["title"], question=data["question"], answer=data["answer"])

    # __repr__  convert object memory address to unambiguous representation for developers, logging and debugging 
    def __repr__(self):
        """the string returned by __repr__ should look like valid python code that could recreate the object"""
        return f"QuizQuestion(title={self.title!r}, question={self.question!r}, answer={self.answer!r})"


    def __str__(self):
        return f"[{self.title}] Q: {self.question} (A: {self.answer})"
class StudySession:

    def __init__(self, title, summary, questions):
        self.title = title
        self.summary = summary
        self.questions = questions

    def to_dict(self) -> dict:
        return {"title":self.title, "summary":self.summary, "questions":[question.to_dict() for question in self.questions]}

    @classmethod
    def from_dict(cls, data: dict):
        questions_list = [QuizQuestion.from_dict(q) for q in data["questions"]]
        return cls(title=data["title"], summary=data["summary"], questions = questions_list)

    ## __repr__  convert object memory address to unambiguous representation for developers, logging and debugging
    def  __repr__(self):
        """the string returned by __repr__ should look like valid python code that could recreate the object"""
        return f"StudySession(title={self.title!r}, summary={self.summary!r}, questions={self.questions!r})"

    # __str__ convert object memory to clear, readable output meant for end user or UI dispay
    def __str__(self):
        """called automatically by print() or str()"""
        return f"[{self.title.upper()}] no_question: {len(self.questions)} "


num1 = QuizQuestion("variable", "is snakecase one of the way of declaring a variable", "True")
num2 = QuizQuestion("class", "class name is declared using camelcase", "True")

new_session = StudySession("variable", "varibles are containers that store data values. They can store string, numbers, booleam, list etc", [num1,num2])
session_dict = new_session.to_dict()
print(session_dict)

rebuild_session = StudySession.from_dict(session_dict)
print(rebuild_session.questions[1].question)
# print(new_session.questions[1].question)

print(repr(num1))
print(num1)

print(repr(new_session))
print(new_session)





