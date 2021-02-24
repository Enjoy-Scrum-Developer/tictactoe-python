from tictactoe.presentation import board, messages
from tictactoe.logic.game_state import GameState, MARK_X, MARK_O
from tictactoe.logic.ai import Ai

BOARD_SIZE = 3
AI_LEVEL = 0 # Lowest AI Level, Highest Level is 2

def create_game():
    state = GameState(BOARD_SIZE)
    return state

def ask_player_to_move(state: GameState):
    input = messages.prompt('Enter a number (from 1 to {}): '
        .format(BOARD_SIZE * BOARD_SIZE))
    state.mark_square(input, MARK_X)
    board.show(state)

def ask_computer_to_move(state: GameState):
    ai = Ai(state)
    no = ai.next_move(AI_LEVEL)
    state.mark_square(no, MARK_O)
    board.show(state)

def start():
    state = create_game()
    board.show(state)
    has_game_ended = False
    winner = None
    while not has_game_ended:
        ask_player_to_move(state)
        has_game_ended, winner = state.has_game_ended()
        if has_game_ended:
            break
        ask_computer_to_move(state)
        has_game_ended, winner = state.has_game_ended()
