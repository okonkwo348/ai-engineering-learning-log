class QuizWuestion:
    def __init__(self, title, question, answer)
        self.title = title
        self.question = question
        self.answer = answer

    def to_dic(self) -> dict:
        """Convert this object into a plain, safe for json.jump()."""
        return {"question": self.question, "answer": self.answer}

    @classmethod
    def from_dict(cls, data: dict):
        """Rebuild a QuizzQuestion object from a plain dic (e.g. loaded from JSON)."""
        return cls(question=data["question"], answer=data["answer"])
