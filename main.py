from game import Game15
from ui import GameUI

def main():
    game = Game15()
    ui = GameUI(game)
    print("Привет! Это игра 'Пятнашки'!")
    print("Расставьте числа по порядку от 1 до 15.")
    game.shuffle(50)
    while True:
        ui.clear_screen()
        ui.show_board()
        ui.show_controls()

        if game.check_win():
            ui.show_win()
            break
        move = ui.get_move()
        if move == '0':
            print("Пока!")
            break
        elif move == 'r':
            game.reset()
            game.shuffle(50)
            ui.show_message("Начинаем заново!")
            continue
        direction = ui.translate_direction(move)
        if game.move(direction):
            ui.show_message(f"Пошли: {direction}")
        else:
            ui.show_error()
        input("Жми Enter чтобы дальше...")
if __name__ == "__main__":
    main()