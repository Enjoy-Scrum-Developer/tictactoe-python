import unittest

from unittest.mock import patch

from tictactoe.logic import game
from tictactoe.logic.ai import Ai

class TestGame(unittest.TestCase):
    @patch.object(Ai, 'next_move')
    @patch('tictactoe.presentation.board.show')
    @patch('tictactoe.presentation.messages.prompt')
    @patch('tictactoe.presentation.messages.alert')
    def test_should_stop_when_player_wins(self, alert, prompt, show, next_move):
        prompt.side_effect = [1, 2, 3]
        next_move.side_effect = [4, 5, 6]
        game.start()
    
    @patch.object(Ai, 'next_move')
    @patch('tictactoe.presentation.board.show')
    @patch('tictactoe.presentation.messages.prompt')
    @patch('tictactoe.presentation.messages.alert')
    def test_should_stop_when_computer_wins(self, alert, prompt, show, next_move):
        prompt.side_effect = [1, 8, 3]
        next_move.side_effect = [4, 5, 6]
        game.start()

    @patch.object(Ai, 'next_move')
    @patch('tictactoe.presentation.board.show')
    @patch('tictactoe.presentation.messages.prompt')
    @patch('tictactoe.presentation.messages.alert')
    def test_should_stop_when_all_squares_marked(self, alert, prompt, show, next_move):
        prompt.side_effect = [5, 9, 3, 4, 8]
        next_move.side_effect = [2, 1, 6, 7]
        game.start()

if __name__ == '__main__':
    unittest.main()
