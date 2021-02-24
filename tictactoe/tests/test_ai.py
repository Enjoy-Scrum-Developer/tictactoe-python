import unittest

import random

from unittest.mock import patch

from tictactoe.logic.ai import Ai
from tictactoe.logic.game_state import GameState, MARK_X, MARK_O

class TestAi(unittest.TestCase):
    @patch.object(Ai, 'get_random_move', return_value=4)
    def test_should_return_random_move_at_level_0(self, get_random_move):
        state = GameState()
        ai = Ai(state)
        state.mark_square(1, MARK_X)
        state.mark_square(2, MARK_O)
        state.mark_square(3, MARK_X)
        move = ai.next_move(0)
        self.assertEqual(4, move)
    def test_should_return_winning_move_at_level_0(self):
        state = GameState()
        ai = Ai(state)
        state.mark_square(5, MARK_X)
        state.mark_square(2, MARK_O)
        state.mark_square(1, MARK_X)
        state.mark_square(9, MARK_O)
        state.mark_square(3, MARK_X)
        state.mark_square(8, MARK_O)
        state.mark_square(3, MARK_X)
        move = ai.next_move(0)
        self.assertEqual(7, move)
    def test_should_return_best_move_at_level_2_start(self):
        state = GameState()
        ai = Ai(state)
        move = ai.next_move(2)
        self.assertEqual(5, move)
    @patch.object(Ai, 'get_random_move', return_value=7)
    def test_should_return_best_move_at_level_2_midgame(self, get_random_move):
        state = GameState()
        ai = Ai(state)
        state.mark_square(5, MARK_X)
        state.mark_square(1, MARK_O)
        move = ai.next_move(2)
        self.assertEqual(7, move)
    def test_should_return_winning_move_at_level_2_midgame(self):
        state = GameState()
        ai = Ai(state)
        state.mark_square(5, MARK_X)
        state.mark_square(1, MARK_O)
        state.mark_square(3, MARK_X)
        state.mark_square(7, MARK_O)
        state.mark_square(6, MARK_X)
        move = ai.next_move(2)
        self.assertEqual(4, move)
    @patch.object(Ai, 'get_random_move', return_value=8)
    def test_should_return_best_move_at_level_2_midgame(self, get_random_move):
        state = GameState()
        ai = Ai(state)
        state.mark_square(5, MARK_X)
        state.mark_square(1, MARK_O)
        state.mark_square(3, MARK_X)
        state.mark_square(7, MARK_O)
        state.mark_square(4, MARK_X)
        state.mark_square(6, MARK_O)
        move = ai.next_move(2)
        self.assertEqual(8, move)

if __name__ == '__main__':
    unittest.main()
