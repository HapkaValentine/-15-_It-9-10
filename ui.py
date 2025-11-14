import os
from game import Game15
class GameUI:
    def __init__(self, game):
        self.igra = game
    def ochistit_ekran(self):
        os.system('cls' if os.name == 'nt' else 'clear')
    def pokazat_pole(self):
        pole = self.igra.poluchit_pole()
        print("\n" + "=" * 25)
        print("    ПЯТНАШКИ")
        print("=" * 25)
        print(f"Сделано ходов: {self.igra.poluchit_schetchik_hodov()}")
        print()
        for i in range(len(pole)):
            print("  +----+----+----+----+")
            print("  |", end="")
            for j in range(len(pole[i])):
                if pole[i][j] == 0:
                    print("    |", end="")
                else:
                    print(f" {pole[i][j]:2} |", end="")
            print()
        print("  +----+----+----+----+")
        print()
    def pokazat_upravlenie(self):
        print("Управление:")
        print("  W - Вверх")
        print("  S - Вниз")
        print("  A - Влево")
        print("  D - Вправо")
        print("  R - Заново")
        print("  0 - Выйти")
        print()
    def poluchit_hod(self):
        while True:
            vvod = input("Ваш ход (W/A/S/D): ").strip().lower()
            if vvod in ['w', 'a', 's', 'd', 'r', '0']:
                return vvod
            else:
                print("Неправильно! Надо W, A, S, D, R или 0")
    def perevesti_napravlenie(self, vvod):
        slovar = {
            'w': 'verh',
            's': 'niz',
            'a': 'levo',
            'd': 'pravo'
        }
        return slovar.get(vvod, vvod)
    def pokazat_soobshenie(self, text):
        print(f"\n{text}")
    def pokazat_pobedu(self):
        hodi = self.igra.poluchit_schetchik_hodov()
        print("\n" + "=" * 40)
        print("УРА! ВЫ ВЫИГРАЛИ!")
        print(f"Всего ходов: {hodi}")
        print("=" * 40)
    def pokazat_oshibku(self):
        print("Так нельзя ходить! Попробуйте по-другому.")