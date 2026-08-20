import DB.printDB as printDB
import Source.listManager as listManager

class MainMenu:

    option = None

    def __init__(self):
        self.printDB = printDB
        self.listManager = listManager.ListManager()

    def display_main_menu(self):
        print(self.printDB.NewLine.new_line +
                self.printDB.MainMenuMessages.main_menu +
                self.printDB.NewLine.new_line +
                self.printDB.NewLine.new_line +
                self.printDB.MainMenuMessages.select_option +
                self.printDB.NewLine.new_line +
                self.printDB.NewLine.new_line +
                '\n'.join(self.printDB.MainMenuMessages.options) +
                self.printDB.NewLine.new_line)

    def selectOption(self):
        self.option = input()

        if self.option == '1':
            print("Viewing Tasks...")
            self.listManager.print_task_list()
            self.display_main_menu()
            self.selectOption()
        elif self.option == '2':
            print("Option 2 Selected")
            task = input("Enter a new task: ")
            self.listManager.add_task(task)
            self.display_main_menu()
            self.selectOption()
        elif self.option == '3':
            print("Option 3 Selected")
            task_id = input("Update task: ")
            self.listManager.edit_list(task_id)
            self.display_main_menu()
            self.selectOption()
        elif self.option == '4':
            print("Option 4 Selected")
            self.listManager.remove_task(task)
            self.display_main_menu()
            self.selectOption()
        elif self.option == '5':
            print("Exiting the application...")
            exit()
        else:
            print(self.printDB.ErrorMessages.invalid_input)
            self.display_main_menu()
            self.selectOption()
