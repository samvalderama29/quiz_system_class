from colorama import init, Fore, Style
init(autoreset = True)
import os.path

class QuizQuestionManager:
    def __init__(self, file_path = "quiz_creator.txt"):
        self.file_path = file_path

    def add_new_question():
        print(Fore.GREEN + Style.BRIGHT + "\n✏️ Enter a new quiz question:")

        with open(quiz_file, "a") as file:
            user_question = input("Question: ")
            choice_a = input("Enter choice a: ")
            choice_b = input("Enter choice b: ")
            choice_c = input("Enter choice c: ")
            choice_d = input("Enter choice d: ")
            correct_answer = input("Correct answer (a/b/c/d): ").lower()

            if correct_answer not in ["a", "b", "c", "d"]:
                print(Fore.RED + "❌ Invalid input! Please choose between a, b, c, and d only.")

            file.write(f"Question: {user_question}\n")
            file.write(f"a) {choice_a}\n")
            file.write(f"b) {choice_b}\n")
            file.write(f"c) {choice_c}\n")
            file.write(f"d) {choice_d}\n")
            file.write(f"Correct answer: {correct_answer}\n")
            file.write("-----\n")

            another_question = input(Fore.CYAN + "\nDo you want to add another question? (yes/no): ")

            if another_question.lower() != "yes":
                print(Fore.RED + "\n❎ Adding questions cancelled.")
                print(Fore.GREEN + "✅ Questions saved successfully!")
                menu_exit_choice()
            else:
                add_new_question()


    def remove_question():
        quiz_file = "quiz_creator.txt"

        print(Fore.GREEN + Style.BRIGHT + "\n🗑️ Remove a quiz question")

        if not os.path.exists(quiz_file):
            print(Fore.RED + "\n❗ No file found to exists")

        with open(quiz_file, "r") as file:
            quiz_creator_file = file.read()

        user_stored_questions = quiz_creator_file.strip().split("-----\n")

        if not user_stored_questions:
            print(Fore.RED + "\n❗ No questions found to exists")

        print(Fore.LIGHTWHITE_EX + "List of Questions:")
        for i, question in enumerate(user_stored_questions):
            first_line = question.splitlines()[0].replace("Question: ", " ") if question else "[Empty]"
            print(
                Fore.YELLOW + f"[{i}]{first_line}")

        try:
            index = int(input(
                Fore.LIGHTWHITE_EX + "Enter the number of the question you want to remove: "))
            if 0 <= index < len(user_stored_questions):
                confirm_remove = input(
                    Fore.BLUE + "\nAre you sure you want to delete this question? (yes/no): ")
                if confirm_remove.lower() == "yes":
                    del user_stored_questions[index]
                    with open(quiz_file,
                              "w") as file:
                        for i, question in enumerate(user_stored_questions):
                            file.write(question.strip() + "\n")
                            if i < len(user_stored_questions) - 1:
                                file.write("-----\n")
                    print(
                        Fore.GREEN + "✅ Question successfully removed!")
                else:
                    print(Fore.LIGHTRED_EX + "❎ Deletion cancelled")
            else:
                print(
                    f"❌ Invalid input. Please enter a number between 0 and {len(user_stored_questions) - 1}")
        except ValueError:
            print("❌ Invalid input. Please enter a valid number.")

        menu_exit_choice()


    def view_all_questions():
        quiz_file = "quiz_creator.txt"

        print(Fore.GREEN + Style.BRIGHT + "\n📝 View all questions")
        print(Fore.LIGHTWHITE_EX + "List of Questions:")

        with open(quiz_file, "r") as file:
            print(file.read())

        if not os.path.exists(quiz_file):
            print(Fore.RED + "❗ No file found to exists")