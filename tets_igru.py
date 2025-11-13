import unittest
from game import Game15


class TestGame15(unittest.TestCase):
    def setUp(self):
        self.game = Game15()

    def test_initial_state(self):
        """Тест начального состояния"""
        board = self.game.get_board()
        self.assertEqual(board[3][3], 0)  # Пустая клетка
        self.assertEqual(board[0][0], 1)  # Первая клетка

    def test_move_valid(self):
        """Тест валидных ходов"""
        # В начальном состоянии можно двигать плитку 15 вверх или 12 влево
        self.assertTrue(self.game.move('up'))
        self.assertEqual(self.game.get_empty_position(), (2, 3))

    def test_move_invalid(self):
        """Тест невалидных ходов"""
        # В начальном состоянии нельзя двигать пустую клетку вниз или вправо
        self.assertFalse(self.game.move('down'))
        self.assertFalse(self.game.move('right'))

    def test_is_solved(self):
        """Тест проверки решения"""
        # Неперемешанная головоломка должна быть решена
        game = Game15()
        self.assertTrue(game.is_solved())

        # После хода головоломка не решена
        game.move('up')
        self.assertFalse(game.is_solved())

    def test_shuffle(self):
        """Тест перемешивания"""
        self.game.shuffle(10)
        self.assertFalse(self.game.is_solved())
        self.assertGreater(self.game.get_moves_count(), 0)


if __name__ == '__main__':
    unittest.main()