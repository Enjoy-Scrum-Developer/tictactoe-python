MARK_X = 'X'
MARK_O = 'O'
BLANK = ' '

class GameState:
    started = False
    size = 0
    squares = []
    def __init__(self, size = 3):
        self.size = size
        self.squares = [BLANK] * (size * size)
    def mark_square(self, no, symbol):
        self.started = True
        index = int(no) - 1
        if self.squares[index] == BLANK:
            self.squares[index] = symbol
            return True
        return False
    @property
    def available_moves(self):
        moves = []
        for index in range(0, self.size * self.size):
            if self.squares[index] == BLANK:
                moves.append(index + 1)
        return moves
    def has_game_ended(self):
        winner = self.find_winner()
        all_squares_marked = self.all_squares_marked()
        return winner != None or all_squares_marked, winner
    def all_squares_marked(self):
        for square in self.squares:
            if square == BLANK:
                return False
        return True
    def find_winner(self):
        horizontal_winner = self.find_winner_on_horizontal()
        if not horizontal_winner == None:
            return horizontal_winner
        vertical_winner = self.find_winner_on_vertical()
        if not vertical_winner == None:
            return vertical_winner
        diagonal_winner = self.find_winner_on_diagonal()
        if not diagonal_winner == None:
            return diagonal_winner
        backward_diagonal_winner = self.find_winner_on_backward_diagonal()
        if not backward_diagonal_winner == None:
            return backward_diagonal_winner
        return None
    def find_winner_on_horizontal(self):
        for row in range(0, self.size):
            tally = {}
            for column in range(0, self.size):
                mark = self.squares[(row * self.size) + column]
                if not mark == BLANK:
                    count = tally.get(mark, 0)
                    tally[mark] = count + 1
            for key, value in tally.items():
                if value == 3:
                    return key
        return None
    def find_winner_on_vertical(self):
        for row in range(0, self.size):
            tally = {}
            for column in range(0, self.size):
                mark = self.squares[row + (column * self.size)]
                if not mark == BLANK:
                    count = tally.get(mark, 0)
                    tally[mark] = count + 1
            for key, value in tally.items():
                if value == 3:
                    return key
        return None
    def find_winner_on_diagonal(self):
        tally = {}
        for row in range(0, self.size):
            mark = self.squares[row * (self.size + 1)]
            if not mark == BLANK:
                count = tally.get(mark, 0)
                tally[mark] = count + 1
        for key, value in tally.items():
            if value == 3:
                return key
        return None
    def find_winner_on_backward_diagonal(self):
        tally = {}
        for row in range(0, self.size):
            mark = self.squares[(row + 1) * (self.size - 1)]
            if not mark == BLANK:
                count = tally.get(mark, 0)
                tally[mark] = count + 1
        for key, value in tally.items():
            if value == 3:
                return key
        return None
