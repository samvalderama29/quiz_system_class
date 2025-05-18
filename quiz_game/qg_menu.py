import sys
from colorama import init, Fore, Style

def main_menu():
    while True:
        print_title()

        print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +  "💡 Welcome to the Quiz Game!")
        print(Fore.LIGHTWHITE_EX + "📚 Test your general knowledge and see how high you can score!")


        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do?")
        print("1️⃣ Play")
        print("2️⃣ Check High Scores")
        print("3️⃣ Exit")

        user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your option (1/2/3): ")

        if user_choice == "1":
            quiz_game_start()
        elif user_choice == "2":
            high_score_view()
        elif user_choice == "3":
            print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!")
            sys.exit()
        else:
            print(Fore.RED +"❌ Invalid input! Please choose between 1, 2, and 3 only.\n")