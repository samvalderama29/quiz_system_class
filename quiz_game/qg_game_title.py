from colorama import init, Fore, Style
from pyfiglet import Figlet

def print_title():
    fig = Figlet(font='bulbhead')
    quiz = fig.renderText('Quiz').splitlines()
    game = fig.renderText('Game').splitlines()
    for quiz_line, game_line in zip(quiz, game):
        print(Fore.MAGENTA + quiz_line + "  " + Fore.CYAN + game_line)
    print(Style.RESET_ALL)
