import unittest

from tictactoe.logic.game_state import GameState, MARK_X, MARK_O, BLANK

class TestGameState(unittest.TestCase):
    def test_should_return_true_on_all_squares_marked(self):
        state = GameState(3)
        state.mark_square(1, MARK_X)
        state.mark_square(2, MARK_O)
        state.mark_square(3, MARK_X)
        state.mark_square(4, MARK_O)
        state.mark_square(5, MARK_X)
        state.mark_square(6, MARK_O)
        state.mark_square(7, MARK_O)
        state.mark_square(8, MARK_X)
        state.mark_square(9, MARK_O)
        self.assertTrue(state.all_squares_marked())
        self.assertEqual([], state.available_moves)
    def test_should_return_false_on_all_squares_marked(self):
        state = GameState(3)
        state.mark_square(5, MARK_X)
        self.assertFalse(state.all_squares_marked())
        self.assertEqual([1, 2, 3, 4, 6, 7, 8, 9], state.available_moves)
    def test_should_return_none_on_find_winner(self):
        state = GameState(3)
        state.mark_square(1, MARK_X)
        self.assertEqual(None, state.find_winner())
    def test_should_return_x_on_find_winner_diagonal(self):
        state = GameState(3)
        state.mark_square(1, MARK_X)
        state.mark_square(5, MARK_X)
        state.mark_square(9, MARK_X)
        self.assertEqual(MARK_X, state.find_winner())
    def test_should_return_x_on_find_winner_backward_diagonal(self):
        state = GameState(3)
        state.mark_square(3, MARK_X)
        state.mark_square(5, MARK_X)
        state.mark_square(7, MARK_X)
        self.assertEqual(MARK_X, state.find_winner())    
    def test_should_return_o_on_find_winner_horizontal_top(self):
        state = GameState(3)
        state.mark_square(1, MARK_O)
        state.mark_square(2, MARK_O)
        state.mark_square(3, MARK_O)
        self.assertEqual(MARK_O, state.find_winner())
    def test_should_return_o_on_find_winner_horizontal_middle(self):
        state = GameState(3)
        state.mark_square(4, MARK_O)
        state.mark_square(5, MARK_O)
        state.mark_square(6, MARK_O)
        self.assertEqual(MARK_O, state.find_winner())
    def test_should_return_o_on_find_winner_horizontal_bottom(self):
        state = GameState(3)
        state.mark_square(7, MARK_O)
        state.mark_square(8, MARK_O)
        state.mark_square(9, MARK_O)
        self.assertEqual(MARK_O, state.find_winner())
    def test_should_return_o_on_find_winner_vertical_left(self):
        state = GameState(3)
        state.mark_square(1, MARK_O)
        state.mark_square(4, MARK_O)
        state.mark_square(7, MARK_O)
        self.assertEqual(MARK_O, state.find_winner())
    def test_should_return_o_on_find_winner_vertical_middle(self):
        state = GameState(3)
        state.mark_square(2, MARK_O)
        state.mark_square(5, MARK_O)
        state.mark_square(8, MARK_O)
        self.assertEqual(MARK_O, state.find_winner())
    def test_should_return_o_on_find_winner_vertical_right(self):
        state = GameState(3)
        state.mark_square(3, MARK_O)
        state.mark_square(6, MARK_O)
        state.mark_square(9, MARK_O)
        self.assertEqual(MARK_O, state.find_winner())

if __name__ == '__main__':
    unittest.main()
