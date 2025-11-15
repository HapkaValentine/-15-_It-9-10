from game import Game15
from ui import GameUI

def main():
    igra = Game15()
    interfeis = GameUI(igra)
    print("Привет! Это игра 'Пятнашки'!")
    print("Расставьте числа по порядку от 1 до 15.")
    igra.peremeshat(50)
    while True:
        interfeis.ochistit_ekran()
        interfeis.pokazat_pole()
        interfeis.pokazat_upravlenie()
        if igra.proverit_pobedu():
            interfeis.pokazat_pobedu()
            break
        vvod_hoda = interfeis.poluchit_hod()
        if vvod_hoda == '0':
            print("Пока!")
            break
        elif vvod_hoda == 'r':
            igra.nachalo()
            igra.peremeshat(50)
            interfeis.pokazat_soobshenie("Начинаем заново!")
            continue
        napravlenie = interfeis.perevesti_napravlenie(vvod_hoda)
        if igra.hodit(napravlenie):
            interfeis.pokazat_soobshenie(f"Пошли: {napravlenie}")
        else:
            interfeis.pokazat_oshibku()
        input("Жми Enter чтобы дальше...")
if __name__ == "__main__":
    main()