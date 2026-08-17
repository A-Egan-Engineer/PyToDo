import DB.printDB as printDB

class MainMenu:

    option = None

    def __init__(self):
        self.printDB = printDB

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

        if self.option == 1:
            print("Option 1 Seleceted")
