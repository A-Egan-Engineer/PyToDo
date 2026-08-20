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

    def remove_task(self, task_id):
        if 0 < task_id < len(self.taskDB.taskList):
            removed_task = self.taskDB.taskList.pop(task_id)
            print(f"Task '{removed_task}' removed successfully.")
        else:
            print(printDB.ErrorMessages.task_not_found)

    def edit_list(self, task_id):
        if 0 < task_id < len(self.taskDB.taskList):
            new_task = input("Enter the updated task: ")
            if new_task:
                self.taskDB.taskList[task_id] = new_task
                print(printDB.SuccessMessages.task_edited)
            else:
                print(printDB.ErrorMessages.invalid_input)
        else:
            print(printDB.ErrorMessages.task_not_found)

    def print_task_list(self):
        if len(self.taskDB.taskList) > 1:
            print(printDB.NewLine.new_line + "Task List:")
            for index, task in enumerate(self.taskDB.taskList[1:], start=1):
                print(f"{index}. {task}")
        else:
            print(printDB.ErrorMessages.task_list_empty)
        