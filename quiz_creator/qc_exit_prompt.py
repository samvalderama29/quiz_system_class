import sys
from colorama import init, Fore, Style
init(autoreset = True)

def menu_exit_choice():
    menu_choice = input(Fore.LIGHTWHITE_EX + "\nWould you like to go back to the menu? (yes/no): ")
    if menu_choice.lower() == "yes":
        return
    elif menu_choice.lower() == "no":
        print(Fore.CYAN + Style.BRIGHT + "\n👋🏽 Goodbye! Thank you. Quiz Creator closed.")
        sys.exit()
    else:
        print(Fore.RED + "❗ Invalid choice! Returning to main menu.")
        return