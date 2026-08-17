import Source.welcome as welcome
import Source.mainMenu as mainMenu

display_welcome = welcome.Welcome()
display_welcome.display_welcome_message()

display_main_menu = mainMenu.MainMenu()
display_main_menu.display_main_menu()
display_main_menu.selectOption()