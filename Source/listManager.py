from DB import taskDB
from DB import printDB

class ListManager:

    def __init__(self):
        self.taskDB = taskDB

    def add_task(self, task):
        if task:
            self.taskDB.taskList.append(task)
            print(printDB.SuccessMessages.task_added)
        else:
            print(printDB.ErrorMessages.invalid_input)

    def print_task_list(self):
        for task in self.taskDB.taskList:
            if task is not None:
                print(f"Task: {task}")
            else:
                print(printDB.ErrorMessages.task_list_empty)