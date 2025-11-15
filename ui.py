import os
from game import Game15
class GameUI:
    def __init__(self, game):
        self.g = game
        self.tmp = 0
    def ochistit_ekran(self):
        kom = "cls"
        if os.name != "nt":
            kom = "clear"
        os.system(kom)
    def pokazat_pole(self):
        p = self.g.poluchit_pole()
        print("\n=======================")
        print("     ИГРА 15 (v1)")
        print("=======================")
        print("Ходы сделаны:", self.g.poluchit_schetchik_hodov())
        print()
        for i in range(len(p)):
            print("  +----+----+----+----+")
            stroka = "  |"
            for j in range(len(p[i])):
                zn = p[i][j]
                if zn == 0:
                    stroka += "    |"
                else:
                    stroka += (" " + str(zn).rjust(2, " ") + " |")
            print(stroka)
        print("  +----+----+----+----+")
        print()
    def pokazat_upravlenie(self):
        print("Управление:")
        print(" W - вверх")
        print(" S - вниз")
        print(" A - влево")
        print(" D - вправо")
        print(" R - рестарт")
        print(" 0 - выход")
        print()
    def poluchit_hod(self):
        h = input("Введите ход: ").strip().lower()
        while h not in ["w", "a", "s", "d", "r", "0"]:
            print("Ошибка. Попробуйте снова.")
            h = input("Введите ход: ").strip().lower()
        return h

    def perevesti_napravlenie(self, h):
        nap = {"w": "verh", "s": "niz", "a": "levo", "d": "pravo"}
        if h in nap:
            return nap[h]
        else:
            return h
    def pokazat_soobshenie(self, t):
        print("\n" + str(t))
    def pokazat_pobedu(self):
        kol = self.g.poluchit_schetchik_hodov()
        print("\n===================================")
        print("          ПОБЕДА !!!")
        print("Вы сделали ходов:", kol)
        print("===================================")
    def pokazat_oshibku(self):
        print("Так ходить нельзя (я сам пробовал).")
