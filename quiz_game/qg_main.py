from qg_game_manager import QuizGameManager
from qg_menu import QuizMainMenu

questions_file = "quiz_creator.txt"
high_score_file = "high_scores.txt"

def main():
    game_manager = QuizGameManager(questions_file, high_score_file)
    main_menu = QuizMainMenu(game_manager)
    game_manager.set_main_menu(main_menu)
    main_menu.main_menu()

if __name__ == "__main__":
    main()