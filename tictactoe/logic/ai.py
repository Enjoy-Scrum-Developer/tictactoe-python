import copy

from random import choice

from tictactoe.logic.game_state import GameState, BLANK, MARK_X, MARK_O

class GameDetails:
    def __init__(self, state: GameState, ai_symbol = MARK_O, player_symbol = MARK_X):
        self.state = state
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol
    def copy_and_switch_symbols(self):
        game_copy = copy.deepcopy(self)
        game_copy.ai_symbol = self.player_symbol
        game_copy.player_symbol = self.ai_symbol
        return game_copy

class SquareEnumerator:
    def __init__(self, state: GameState):
        self.state = state
    def enumerate_horizontal(self, index: int):
        return self.enumerate(self.build_horizontal_index_enumerator, index)
    def enumerate_vertical(self, index: int):
        return self.enumerate(self.build_vertical_index_enumerator, index)
    def enumerate_diagonal(self, index: int):
        return self.enumerate(self.build_diagonal_index_enumerator, index)
    def enumerate_backward_diagonal(self, index: int):
        return self.enumerate(self.build_backward_diagonal_index_enumerator, index)
    def enumerate(self, builder, index):
        index_symbols = {}
        enumerate_squares = builder(index)
        for index in range(0, self.state.size):
            square_index = enumerate_squares(index)
            index_symbols[square_index] = self.state.squares[square_index]
        return index_symbols.items()
    def build_horizontal_index_enumerator(self, row: int):
        return lambda column : row * self.state.size + column
    def build_vertical_index_enumerator(self, column: int):
        return lambda row : row * self.state.size + column
    def build_diagonal_index_enumerator(self, index):
        return lambda row : row * self.state.size + row
    def build_backward_diagonal_index_enumerator(self, index):
        return lambda row : (row + 1) * (self.state.size - 1)

class SquareScoresBuilder:
    def __init__(self, game: GameDetails):
        self.ai_symbol = game.ai_symbol
        self.player_symbol = game.player_symbol
        self.state = game.state
        self.size = game.state.size
        self.scores = [0] * (game.state.size * game.state.size)
    def build(self):
        enumerator = SquareEnumerator(self.state)
        self.iterate_and_compute_scores(self.size, enumerator.enumerate_horizontal)
        self.iterate_and_compute_scores(self.size, enumerator.enumerate_vertical)
        self.iterate_and_compute_scores(1, enumerator.enumerate_diagonal)
        self.iterate_and_compute_scores(1, enumerator.enumerate_backward_diagonal)
        for index in range(0, self.size * self.size):
            if self.scores[index] == None:
                self.scores[index] = -1
        return self.scores
    def iterate_and_compute_scores(self, iteration_count, enumerator_function):
        for iteration in range(0, iteration_count):
            player_marks = 0
            items = enumerator_function(iteration)
            for index, symbol in items:
                if not symbol == BLANK:
                    self.scores[index] = None
                if symbol == self.player_symbol:
                    player_marks += 1
            if player_marks == 0:
                for index, symbol in items:
                    if not self.scores[index] == None:
                        self.scores[index] += 1

class Ai:
    def __init__(self, state: GameState, ai_symbol = MARK_O, player_symbol = MARK_X):
        self.state = state
        self.ai_symbol = ai_symbol
        self.player_symbol = player_symbol
    def next_move(self, ai_level: int):
        game = GameDetails(self.state, self.ai_symbol, self.player_symbol)
        return self.compute(ai_level, self.state.available_moves, game)
    def compute(self, ai_level: int, best_moves: [], game: GameDetails):
        winning_move = self.find_winning_move(game.state, game.ai_symbol)
        if not winning_move == None:
            return winning_move
        if ai_level == 0:
            return self.get_random_move(best_moves)
        winning_move = self.find_winning_move(game.state, game.player_symbol)
        if not winning_move == None:
            return winning_move
        if ai_level == 1:
            return self.get_random_move(best_moves)
        return self.find_best_move(game)
    def find_best_move(self, game: GameDetails):
        square_scores = SquareScoresBuilder(game).build()
        max_score = max(square_scores)
        if square_scores.count(max_score) > 1:
            best_moves = []
            for index, value in enumerate(square_scores):
                if value == max_score:
                    best_moves.append(index)
            return self.get_random_move(best_moves)
        return square_scores.index(max_score) + 1
    def find_winning_move(self, state: GameState, symbol: str):
        for no in state.available_moves:
            state_copy = copy.deepcopy(state)
            if state_copy.mark_square(no, symbol):
                if state_copy.find_winner() == symbol:
                    return no
        return None
    def get_random_move(self, available_moves: []):
        return choice(available_moves)
