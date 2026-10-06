from gemini_lesson.ask_gemini import generate_study_session
import logging
import sys

import json
class QuizQuestion:
    def __init__(self, title: str, question: str, answer: str) -> None:
        self.title = title
        self.question = question
        self.answer = answer

    def to_dict(self) -> dict[str,str]:
        """Convert this object into a plain, safe for json.jump()."""
        return {"title": self.title, "question": self.question, "answer": self.answer}

    @classmethod
    def from_dict(cls, data: dict) -> "QuizQuestion":
        """Rebuild a QuizzQuestion object from a plain dic (e.g. loaded from JSON)."""
        return cls(title=data["title"], question=data["question"], answer=data["answer"])

    # __repr__  convert object memory address to unambiguous representation for developers, logging and debugging 
    def __repr__(self) -> str:
        """the string returned by __repr__ should look like valid python code that could recreate the object"""
        return f"QuizQuestion(title={self.title!r}, question={self.question!r}, answer={self.answer!r})"


    def __str__(self) -> str:
        return f"[{self.title}] Q: {self.question} (A: {self.answer})"


class StudySession:

    def __init__(self, title: str, summary: str, questions: list[QuizQuestion]) -> None:
        self.title = title
        self.summary = summary
        self.questions = questions

    def to_dict(self) -> dict:
        return {"title":self.title, "summary":self.summary, "questions":[question.to_dict() for question in self.questions]}

    @classmethod
    def from_dict(cls, data: dict) -> "StudySession":
        questions_list = [QuizQuestion.from_dict(q) for q in data["questions"]]
        return cls(title=data["title"], summary=data["summary"], questions = questions_list)

    ## __repr__  convert object memory address to unambiguous representation for developers, logging and debugging
    def  __repr__(self) -> str:
        """the string returned by __repr__ should look like valid python code that could recreate the object"""
        return f"StudySession(title={self.title!r}, summary={self.summary!r}, questions={self.questions!r})"

    # __str__ convert object memory to clear, readable output meant for end user or UI dispay
    def __str__(self) -> str:
        """called automatically by print() or str()"""
        return f"[{self.title.upper()}] no_question: N {len(self.questions)} "

def load_sessions(filename: str) -> list[StudySession]:
        try:
            with open(filename, "r") as file:
                list_dicts = json.load(file)
                sessions = [StudySession.from_dict(each_dict) for each_dict in list_dicts]
                return sessions
        except (FileNotFoundError, json.JSONDecodeError):
            return []

def save_sessions(sessions: list[StudySession], filename: str) -> None:
    with open(filename, "w") as file:
        json.dump([session.to_dict() for session in sessions], file)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def main() -> None:

    is_running = True
    while is_running:

        input_var = input( ": Enter: 'new' to add tasks, 'list' to list all tasks, "
            "'view' to view a task, 'exit' to quit > ")

        if input_var == "new":
            topic = input("What topic or have in mind? > ")
            result = generate_study_session(topic)
            if result is None:
                logger.error("No data received")
                continue

            new_session = StudySession.from_dict(result)
            tasks = load_sessions("storage.json")
            tasks.append(new_session)
            save_sessions(tasks, "storage.json")

        elif input_var == "list":
            total_session = load_sessions("storage.json")
            for session in total_session:
                print(str(session))

        elif input_var == "view":
            title_input = input("What do you want to view? >")
            tasks = load_sessions("storage.json")
            similar_search = []

            for session in tasks:
                if title_input.lower() in session.title.lower():
                    similar_search.append(session)

            if len(similar_search) == 0:
                print(f"{title_input} does not exist")

            elif len(similar_search) == 1:
                    print(similar_search[0])

            elif len(similar_search) > 1:    
                print(f"There are more than one {title_input}. You will have to select one")
                try:
                    select_one = int(input("To Select: Enter a valid digit eg 1, 2, 3,.. >"))
                    print(similar_search[select_one - 1])
                except ValueError:
                    print("please enter a digit: 1, 2, 3,.... ")
                    continue



        elif input_var == "exit":
            is_running = False
            
        else:
            continue

                 


            


if __name__ == "__main__":
    main()


    # result = generate_study_session("a paragraph about Python functions")
    # if result is None:
    #     logger.error("No data received")
    #     sys.exit()

    # new_session = StudySession.from_dict(result)
    # tasks = load_sessions("storage.json")
    # tasks.append(new_session)
    # save_sessions(tasks, "storage.json")
    # print(repr(new_session))


# num1 = QuizQuestion("variable", "is snakecase one of the way of declaring a variable", "True")
# num2 = QuizQuestion("class", "class name is declared using camelcase", "True")

# new_session = StudySession("variable", "varibles are containers that store data values. They can store string, numbers, booleam, list etc", [num1,num2])
# session_dict = new_session.to_dict()
# print(session_dict)

# print(new_session.questions[0].question)
# print(new_session.questions[1].question)

# print(repr(num1))
# print(num1)









