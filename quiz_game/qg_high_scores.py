import sys
import os
from colorama import init, Fore, Style

def save_high_score(player_name, current_score):
    with open(high_score_file, "a") as file:
        file.write(f"{player_name}: {current_score}\n")


def high_score_view():
    if not os.path.exists(high_score_file):
        print(Fore.YELLOW + "⚠️ No high scores yet.")
        return

    print()
    print_title()
    print(Fore.LIGHTGREEN_EX + "🏆 High Scores 🏆")

    scores = []
    with open(high_score_file, "r") as file:
        for name_line in file:
            player_name, player_score = name_line.strip().rsplit(":", 1)
            scores.append((int(player_score), player_name))

    scores.sort(reverse = True)

    for score, name in scores:
        print(f"{name}: {score}")