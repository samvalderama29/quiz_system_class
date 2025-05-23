import os
from colorama import init, Fore, Style
init(autoreset = True)
from qg_game_title import ASCIITitle

class HighScoresManager:
    def __init__(self, high_score_file):
        self.high_score_file_path = high_score_file
        self.game_title = ASCIITitle()

    def save_high_score(self, player_name, current_score):
        with open(self.high_score_file_path, "a") as file:
            file.write(f"{player_name}: {current_score}\n")

    def high_score_view(self):
        if not os.path.exists(self.high_score_file_path):
            print(Fore.YELLOW + "⚠️ No high scores yet.")
            return

        print()
        self.game_title.print_title()
        print(Fore.LIGHTGREEN_EX + "🏆 High Scores 🏆")

        scores = []
        with open(self.high_score_file_path, "r") as file:
            for name_line in file:
                player_name, player_score = name_line.strip().rsplit(":", 1)
                scores.append((int(player_score), player_name))

        scores.sort(reverse = True)

        for score, name in scores:
            print(f"{name}: {score}")