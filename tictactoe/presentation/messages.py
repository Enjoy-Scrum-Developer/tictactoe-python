from tictactoe.helpers.ansi import bcolors

def alert(message):
    print(bcolors.YELLOW + message + bcolors.END)

def prompt(message):
    return input(bcolors.GREEN + message + bcolors.END)
