from game import Game15
from ui import GameUI

def main():
    g = Game15()
    interface = GameUI(g)
    print("Добро пожаловать в игру Пятнашки!")
    print("Нужно собрать числа в правильном порядке.")
    print("Если что, можно перезапустить игру буквой r.")
    shuffle_times = 50
    g.peremeshat(shuffle_times)
    is_running = True
    while is_running:
        interface.ochistit_ekran()
        interface.pokazat_pole()
        interface.pokazat_upravlenie()
        if g.proverit_pobedu():
            interface.pokazat_pobedu()
            is_running = False
            input("Нажмите Enter чтобы выйти...")
            break
        player_input = interface.poluchit_hod()
        if player_input == "0":
            print("Выход из игры. Пока!")
            break
        if player_input == "r":
            g.nachalo()
            g.peremeshat(50)
            interface.pokazat_soobshenie("Перезапуск выполнен!")
            input("Enter...")
            continue
        move_dir = interface.perevesti_napravlenie(player_input)
        if move_dir is None:
            print("Непонятно что вы ввели...")
            input("Enter...")
            continue
        moved = g.hodit(move_dir)
        if moved:
            interface.pokazat_soobshenie("Ход сделан: " + move_dir)
        else:
            interface.pokazat_oshibku()
        tmp = input("Нажмите Enter...")
if __name__ == "__main__":
    main()
