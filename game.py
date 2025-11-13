
import random
from typing import List, Tuple, Optional


class Game15:
    def __init__(self):
        self.size = 4
        self.board = []
        self.empty_pos = (3, 3)
        self.moves_count = 0
        self.reset_game()

    def reset_game(self) -> None:
        """Инициализация игрового поля с правильной последовательностью"""
        self.board = []
        number = 1
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    row.append(0)  # Пустая клетка
                else:
                    row.append(number)
                    number += 1
            self.board.append(row)
        self.empty_pos = (self.size - 1, self.size - 1)
        self.moves_count = 0

    def shuffle(self, moves: int = 1000) -> None:
        """Перемешивание поля совершая случайные ходы"""
        directions = ['up', 'down', 'left', 'right']
        for _ in range(moves):
            direction = random.choice(directions)
            self.move(direction)

    def move(self, direction: str) -> bool:
        """Перемещение пустой клетки в указанном направлении"""
        x, y = self.empty_pos

        if direction == 'up' and x > 0:
            self.board[x][y], self.board[x - 1][y] = self.board[x - 1][y], self.board[x][y]
            self.empty_pos = (x - 1, y)
            self.moves_count += 1
            return True

        elif direction == 'down' and x < self.size - 1:
            self.board[x][y], self.board[x + 1][y] = self.board[x + 1][y], self.board[x][y]
            self.empty_pos = (x + 1, y)
            self.moves_count += 1
            return True

        elif direction == 'left' and y > 0:
            self.board[x][y], self.board[x][y - 1] = self.board[x][y - 1], self.board[x][y]
            self.empty_pos = (x, y - 1)
            self.moves_count += 1
            return True

        elif direction == 'right' and y < self.size - 1:
            self.board[x][y], self.board[x][y + 1] = self.board[x][y + 1], self.board[x][y]
            self.empty_pos = (x, y + 1)
            self.moves_count += 1
            return True

        return False

    def is_solved(self) -> bool:
        """Проверка, решена ли головоломка"""
        expected = 1
        for i in range(self.size):
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    if self.board[i][j] != 0:
                        return False
                else:
                    if self.board[i][j] != expected:
                        return False
                    expected += 1
        return True

    def get_board(self) -> List[List[int]]:
        """Возвращает текущее состояние поля"""
        return self.board

    def get_empty_position(self) -> Tuple[int, int]:
        """Возвращает позицию пустой клетки"""
        return self.empty_pos

    def get_moves_count(self) -> int:
        """Возвращает количество сделанных ходов"""
        return self.moves_count

    def is_valid_move(self, direction: str) -> bool:
        """Проверка возможности хода в указанном направлении"""
        x, y = self.empty_pos

        if direction == 'up' and x > 0:
            return True
        elif direction == 'down' and x < self.size - 1:
            return True
        elif direction == 'left' and y > 0:
            return True
        elif direction == 'right' and y < self.size - 1:
            return True

        return False