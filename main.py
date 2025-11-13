from game import Game15
from ui import GameUI


def main():
    # Инициализация игры и интерфейса
    game = Game15()
    ui = GameUI(game)

    print("Добро пожаловать в игру 'Пятнашки'!")
    print("Перемещайте плитки, чтобы упорядочить числа от 1 до 15.")

    # Перемешивание поля
    game.shuffle(50)

    # Главный игровой цикл
    while True:
        ui.clear_screen()
        ui.display_board()
        ui.display_controls()

        # Проверка победы
        if game.is_solved():
            ui.show_victory()
            break

        # Получение хода от пользователя
        move = ui.get_move()

        # Обработка специальных команд
        if move == '0':
            print("Спасибо за игру!")
            break
        elif move == 'r':
            game.reset_game()
            game.shuffle(50)
            ui.show_message("Игра перезапущена!")
            continue

        # Выполнение хода
        direction = ui.convert_input(move)
        if game.move(direction):
            ui.show_message(f"Ход выполнен: {direction}")
        else:
            ui.show_invalid_move()

        input("Нажмите Enter для продолжения...")


if __name__ == "__main__":
    main()