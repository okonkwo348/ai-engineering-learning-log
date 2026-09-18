#  class Task:

#     container = {}
#     def __init__(self):
#         self.title = title
#         self.done = done


# class TaskManager:
#     def __init__(self):
#         self.container = container
    
#     def add_tasks(self, title):
#         container[self.title] = "not-done"
        

#     def list_all_tasks(self, title, done):
#         return container

#     def mark_task(self, title, done):
#         container[self.title] = {self.done}
    
#     def save():
#         with open("note.txt","w") as file:
#             file.write(key, val  for key, val in container)

#     def load():
#         pass


    # while True:
    #     input("type the follow:\n 'add': to add a tasks\n 'list': to know the list of tasks\n 'done': to mark done to a tasks\n 'exit': to end the program")

    

import logging
import json
from pathlib import Path


def load_task():
        try:
            with open("file.json", "r") as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    

tasks = load_task()


def add_tasks(new_task):
    tasks.append({"title" :new_task, "done":False})

def list_all_task():
    if tasks is None:
            return f"Empty: add one tas...eg resting, cleaning"
    else:
        return tasks

def mark_task(index_list):
    global tasks
    if tasks is None:
        tasks = []
    tasks[index_list]["done"] = True
    

def save_task():
    with open("file.json", "w") as file:
        json.dump(tasks, file, indent=2)

    


        

logging.basicConfig(level = logging.INFO)
logger = logging.getLogger(__name__)

select = True
while select:
    print("Welcome to Todo App!")
    select =   input(": Enter: 'add' to add tasks, 'list' to list all tasks, 'done' to mark a tasks done, 'exit' to quite > ")
    select = select.lower().strip()

    if select == "add":
        new_task = input(" Enter tasks e.g 'sweep', sleep'....>")
        add_tasks(new_task)
        save_task()

    elif select == "list":
        print(list_all_task())

    elif select == "done":
        index_list = input("Enter the tasks no: ")
        try:
            mark_task(int(index_list))
        except (ValueError, IndexError) as e:
            logger.error(f"Index of List out of range {e}")
        
        try:
            save_task()
        except FileNotFoundError as e:
            logger.error(f"File Not found {e}")

            


    elif select == "exit":
        select = False

        


    
