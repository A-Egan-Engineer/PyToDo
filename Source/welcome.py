import DB.printDB as printDB

class Welcome:
    def __init__(self):
        self.printDB = printDB

    def display_welcome_message(self):
        print(self.printDB.NewLine.new_line + 
              self.printDB.WelcomeMessages.welcome + 
              self.printDB.NewLine.new_line + 
              self.printDB.NewLine.new_line +
              self.printDB.WelcomeMessages.description + 
              self.printDB.NewLine.new_line)