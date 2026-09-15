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
#         with open("note.txt","w") as f:
#             f.write(key, val  for key, val in container)

#     def load():
#         pass


#     while True:
#         input("type the follow:\n 'add': to add a task\n 'list': to know the list of task\n 'done': to mark done to a task\n 'exit': to end the program")

    

# import logging


# task = [
#     {"title": "sweep", "done":False},
#     {"title": "cook", "done":False},
#     {"title": "brush", "done":False},
#     {"title": "wash", "done":False},
#     {"title": "read", "done":False},
#     ]


# def add_tasks(new_task):
#     task.append({"title" :new_task, "done":False})

# def list_all_task():
#     return task

# def mark_task(index_list):
#     task[index_list]["done"] = True

# def save_task():
#     with open("file.json", "a") as f:
#         for i in task: 
#             f.write(str(i))

# def load_task():
#     with open("file.json", "r") as f:
#         task = f.readlines()

# logging.basicConfig(level = logging.INFO)
# logger = logging.getLogger(__name__)
# select = True
# while select:
#     load_task()
#     print("Welcome to Todo App!")
#     select =   input(": Enter: 'add' to add task, 'list' to list all tasks, 'done' to mark a task done, 'exit' to quite ")

#     if select == "add":
#         new_task = input(" Enter task e.g 'sweep', sleep'....")
#         add_tasks(new_task)

#     elif select == "list":
#         print(list_all_task())

#     elif select == "done":
#         index_list = input("Enter the task no: ")
#         try:
#             mark_task(int(index_list))
#         except IndexError as e:
#             logger.error(f"Index of List out of range {e}")
#         try:
#             save_task()
#         except FileNotFoundError as e:
#             logger.error(f"File Not found {e}")


#     elif select == "exit":
#         select = False

        


    
