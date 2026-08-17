# This file acts as the Database for the PyToDo app messages, providing a simple way to store and retrieve data.

# Welcome message for the PyToDo app

class WelcomeMessages:
    welcome = "Welcome to PyToDo!"
    description = "PyToDo is a simple command-line to-do list application that helps you manage your tasks efficiently."

class MainMenuMessages:
    main_menu = "Main Menu"
    select_option = "Please select and option from the below:"
    options = ["1. View Tasks",
               "2. Add Task",
               "3. Edit Task",
               "4. Delete Task",
               "5. Exit"
              ]

class NewLine:
    new_line = "\n"

# Error messages for the PyToDo app
class ErrorMessages:
    invalid_input = "Invalid input. Please try again."
    task_not_found = "Task not found. Please check the task ID and try again."
    database_error = "Database error. Please try again later."
