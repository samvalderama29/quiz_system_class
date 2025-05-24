import sys
from colorama import init, Fore, Style
init(autoreset = True)
from qg_game_title import ASCIITitle

class QuizMainMenu:
    def __init__(self, quiz_game_path):
        self.quiz_game_path = quiz_game_path

    def main_menu(self):
        while True:
            ASCIITitle.print_title()

            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT +  "💡 Welcome to the Quiz Game!")
            print(Fore.LIGHTWHITE_EX + "📚 Test your general knowledge and see how high you can score!")

            print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do?")
            print("1️⃣ Play")
            print("2️⃣ Check High Scores")
            print("3️⃣ Exit")

            user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your option (1/2/3): ")

            if user_choice == "1":
                self.quiz_game_path.quiz_game_start()
            elif user_choice == "2":
                self.quiz_game_path.score_manager.high_score_view()
            elif user_choice == "3":
                print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!")
                sys.exit()
            else:
                print(Fore.RED +"❌ Invalid input! Please choose between 1, 2, and 3 only.\n")