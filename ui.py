import os
from game import Game15
class GameUI:
    def __init__(self, game: Game15):
        self.game = game

    def clear_screen(self) -> None:
        """Очистка экрана консоли"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_board(self) -> None:
        """Отображение игрового поля"""
        board = self.game.get_board()

        print("\n" + "=" * 25)
        print("    ПЯТНАШКИ")
        print("=" * 25)
        print(f"Ходов сделано: {self.game.get_moves_count()}")
        print()

        for i in range(len(board)):
            print("  +----+----+----+----+")
            print("  |", end="")
            for j in range(len(board[i])):
                if board[i][j] == 0:
                    print("    |", end="")
                else:
                    print(f" {board[i][j]:2} |", end="")
            print()
        print("  +----+----+----+----+")
        print()

    def display_controls(self) -> None:
        """Отображение управления"""
        print("Управление:")
        print("  W - Вверх")
        print("  S - Вниз")
        print("  A - Влево")
        print("  D - Вправо")
        print("  R - Перезапуск")
        print("  0 - Выход")
        print()
    def get_move(self) -> str:
        """Получение хода от пользователя"""
        while True:
            move = input("Ваш ход (W/A/S/D): ").strip().lower()

            if move in ['w', 'a', 's', 'd', 'r', '0']:
                return move
            else:
                print("Неверный ввод! Используйте W, A, S, D, R или 0")

    def convert_input(self, move: str) -> str:
        """Конвертация ввода пользователя в направление"""
        conversion = {
            'w': 'up',
            's': 'down',
            'a': 'left',
            'd': 'right'
        }
        return conversion.get(move, move)

    def show_message(self, message: str) -> None:
        """Отображение сообщения"""
        print(f"\n{message}")

    def show_victory(self) -> None:
        """Отображение сообщения о победе"""
        moves = self.game.get_moves_count()
        print("\n" + "=" * 40)
        print("🎉 ПОЗДРАВЛЯЮ! ВЫ РЕШИЛИ ГОЛОВОЛОМКУ! 🎉")
        print(f"Количество ходов: {moves}")
        print("=" * 40)

    def show_invalid_move(self) -> None:
        """Отображение сообщения о недопустимом ходе"""
        print("Невозможно сделать этот ход! Попробуйте другой.")