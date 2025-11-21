import unittest
from game import Game15

class TestGame15(unittest.TestCase):
    def setUp(self):
        self.game = Game15()

    def test_initial_state(self):
        board = self.game.get_board()
        self.assertEqual(board[3][3], 0)
        self.assertEqual(board[0][0], 1)

    def test_valid_moves(self):
        self.assertTrue(self.game.move('up'))
        self.assertEqual(self.game.get_empty_pos(), (2, 3))

    def test_invalid_moves(self):
        self.assertFalse(self.game.move('down'))
        self.assertFalse(self.game.move('right'))

    def test_win_condition(self):
        game = Game15()
        self.assertTrue(game.check_win())

        game.move('up')
        self.assertFalse(game.check_win())

    def test_shuffle(self):
        self.game.shuffle(10)
        self.assertFalse(self.game.check_win())
        self.assertGreater(self.game.get_moves_count(), 0)

if __name__ == '__main__':
    unittest.main()