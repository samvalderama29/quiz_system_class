from colorama import init, Fore, Style
init(autoreset = True)
from pyfiglet import Figlet

class ASCIITitle:
    @staticmethod
    def print_title():
        fig = Figlet(font='bulbhead')
        quiz = fig.renderText('Quiz').splitlines()
        game = fig.renderText('Game').splitlines()
        for quiz_line, game_line in zip(quiz, game):
            print(Fore.MAGENTA + quiz_line + "  " + Fore.CYAN + game_line)
        print(Style.RESET_ALL)