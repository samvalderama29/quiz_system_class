import sys
from colorama import init, Fore, Style
init(autoreset = True)

class ExitPromptMenu:
    def __init__(self, exit_menu = None):
        self.exit_menu_path = exit_menu

    def menu_exit_choice(self):
        menu_choice = input(Fore.LIGHTWHITE_EX + "Would you like to go back to the menu? (yes/no): ")
        if menu_choice.lower() == "yes":
            print()
            if self.exit_menu_path:
                self.exit_menu_path()
            return
        elif menu_choice.lower() == "no":
            print(Fore.CYAN + Style.BRIGHT + "\n👋🏽 Goodbye! Thank you. Quiz Creator closed.")
            sys.exit()
        else:
            print(Fore.RED + "❗ Invalid choice! Returning to main menu.")
            return