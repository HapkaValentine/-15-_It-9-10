import os

class GameUI:
    def __init__(self, game):
        self.game = game

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def show_board(self):
        board = self.game.get_board()

        print("\n" + "=" * 25)
        print("    ПЯТНАШКИ")
        print("=" * 25)
        print(f"Сделано ходов: {self.game.get_moves_count()}")
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

    def show_controls(self):
        print("Управление:")
        print("  W - Вверх")
        print("  S - Вниз")
        print("  A - Влево")
        print("  D - Вправо")
        print("  R - Заново")
        print("  0 - Выйти")
        print()

    def get_move(self):
        while True:
            move = input("Ваш ход (W/A/S/D): ").strip().lower()
            
            if move in ['w', 'a', 's', 'd', 'r', '0']:
                return move
            else:
                print("Неправильно! Надо W, A, S, D, R или 0")

    def translate_direction(self, move):
        if move == 'w': return 'up'
        if move == 's': return 'down'
        if move == 'a': return 'left'
        if move == 'd': return 'right'
        return move

    def show_message(self, text):
        print(f"\n{text}")

    def show_win(self):
        moves = self.game.get_moves_count()
        print("\n" + "=" * 40)
        print("УРА! ВЫ ВЫИГРАЛИ!")
        print(f"Всего ходов: {moves}")
        print("=" * 40)

    def show_error(self):
        print("Так нельзя ходить! Попробуйте по-другому.")