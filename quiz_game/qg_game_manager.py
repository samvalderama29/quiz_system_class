import random
from colorama import init, Fore, Style

def quiz_game_play(player_name):
    questions_list = load_questions()
    if not questions_list:
        return

    random.shuffle(questions_list)
    current_score = 0
    incorrect_attempts = 0
    max_allowed_incorrect = 5
    question_log = []

    for current_question in questions_list:
        if incorrect_attempts >= max_allowed_incorrect:
            break

        print(Fore.LIGHTBLACK_EX + f"\n⭐ Score: {current_score} | ❌ Mistakes: {incorrect_attempts}/{max_allowed_incorrect}")

        print(Fore.LIGHTYELLOW_EX+ f"\nQuestion: {current_question["file_question"]}")
        print(f"a) {current_question["option_a"]}")
        print(f"b) {current_question["option_b"]}")
        print(f"c) {current_question["option_c"]}")
        print(f"d) {current_question["option_d"]}")

        while True:
            player_answer = input(Fore.LIGHTWHITE_EX + "Your answer (a/b/c/d): ").strip()

            if player_answer.isupper():
                print(Fore.RED + "⚠️ Capital letters are not allowed. Please use lowercase only (a/b/c/d).")
                continue
            if player_answer in ['a', 'b', 'c', 'd']:
                break
            print(Fore.RED + "⚠️ Please enter a valid option (a/b/c/d).")

        if player_answer == current_question["correct_answer"]:
            print(Fore.GREEN + "✅ Correct!")
            current_score += 1
        else:
            print(Fore.RED + f"❌ Wrong! Correct answer was: {current_question["correct_answer"]}")
            incorrect_attempts += 1

        question_log.append((current_question["file_question"], player_answer, current_question["correct_answer"]))

    if current_score == len(questions_list):
        print(Fore.LIGHTCYAN_EX + f"\nFinal Score: {current_score}")
        print(Fore.GREEN + "🎉 Congratulations! You got a perfect score! 🎉")
    else:
        print(Fore.RED + "\n🛑 GAME OVER 🛑")
        print(Fore.LIGHTCYAN_EX + f"\nFinal Score: {current_score}")

    save_high_score(player_name, current_score)

    while True:
        print(Fore.LIGHTYELLOW_EX + "\nWhat would you like to do next?")
        print("🕹️ 1. Play Again")
        print("📄 2. View Answer Key")
        print("🏠 3. Main Menu")
        print("🚪 4. Exit")

        game_choice = input(Fore.LIGHTWHITE_EX + "Choose an option: ")


        if game_choice == "1":
            quiz_game_play(player_name)
        elif game_choice == "2":
            view_answer_key(question_log)
            menu_exit_choice()
        elif game_choice == "3":
            main_menu()
        elif game_choice == "4":
            print(Fore.CYAN + Style.BRIGHT + "👋 Goodbye. Thank you for playing!")
            break
        else:
            print(Fore.RED + "❌ Invalid input! Please choose between 1, 2, 3, and 4 only.\n")

def view_answer_key(history):
    print(Fore.LIGHTBLUE_EX + "\n📘 Answer Key")
    for i, (question, given, correct) in enumerate(history, 1):
        print(Fore.LIGHTYELLOW_EX + f"{i}. {question}")
        print(f"Your Answer: {given}")
        print(f"Correct Answer: {correct}\n")