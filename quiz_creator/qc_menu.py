from colorama import init, Fore, Style
init(autoreset = True)
from qc_question_manager import QuizQuestionManager
import sys

class QuizMenuManager:
    def __init__(self):
        self.question_manager = QuizQuestionManager()

    def main_menu(self):
        while True:
            print(Fore.LIGHTMAGENTA_EX + Style.BRIGHT + "\n📚 Welcome to the Quiz Creator!")
            print(Fore.LIGHTWHITE_EX + "💡 This program allows you to create questions and input answer to make a quiz!")
            print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do?")

            print(f"{Fore.GREEN}1. {Fore.RESET}Add a question")
            print(f"{Fore.CYAN}2. {Fore.RESET}Remove a question")
            print("3. View all questions")
            print(f"{Fore.RED}4. {Fore.RESET}Exit")

            user_choice = input(Fore.LIGHTYELLOW_EX + "Enter your choice (1/2/3/4): ")

            if user_choice == "1":
                self.question_manager.add_new_question()
            elif user_choice == "2":
                self.question_manager.remove_question()
            elif user_choice == "3":
                self.question_manager.view_all_questions()
            elif user_choice == "4":
                print(Fore.CYAN + Style.BRIGHT + "\n👋🏽 Goodbye! Thank you. Quiz Creator closed.")
                sys.exit()
            else:
                print(Fore.RED +"\n❌ Invalid input! Please choose between 1, 2, 3, and 4 only.")