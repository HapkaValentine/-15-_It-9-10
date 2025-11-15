import random
class Game15:
    def __init__(self):
        self.razmer = 4
        self.pole = []
        self.pustaya_poziciya = (3, 3)
        self.schetchik_hodov = 0
        self.nachalo()
    def nachalo(self):
        self.pole = []
        chislo = 1
        for i in range(self.razmer):
            ryad = []
            for j in range(self.razmer):
                if i == self.razmer - 1 and j == self.razmer - 1:
                    ryad.append(0)
                else:
                    ryad.append(chislo)
                    chislo += 1
            self.pole.append(ryad)
        self.pustaya_poziciya = (self.razmer - 1, self.razmer - 1)
        self.schetchik_hodov = 0
    def peremeshat(self, skolko=1000):
        napravleniya = ['verh', 'niz', 'levo', 'pravo']
        for _ in range(skolko):
            kuda = random.choice(napravleniya)
            self.hodit(kuda)
    def hodit(self, kuda):
        x, y = self.pustaya_poziciya
        if kuda == 'verh' and x > 0:
            self.pole[x][y], self.pole[x - 1][y] = self.pole[x - 1][y], self.pole[x][y]
            self.pustaya_poziciya = (x - 1, y)
            self.schetchik_hodov += 1
            return True
        elif kuda == 'niz' and x < self.razmer - 1:
            self.pole[x][y], self.pole[x + 1][y] = self.pole[x + 1][y], self.pole[x][y]
            self.pustaya_poziciya = (x + 1, y)
            self.schetchik_hodov += 1
            return True
        elif kuda == 'levo' and y > 0:
            self.pole[x][y], self.pole[x][y - 1] = self.pole[x][y - 1], self.pole[x][y]
            self.pustaya_poziciya = (x, y - 1)
            self.schetchik_hodov += 1
            return True
        elif kuda == 'pravo' and y < self.razmer - 1:
            self.pole[x][y], self.pole[x][y + 1] = self.pole[x][y + 1], self.pole[x][y]
            self.pustaya_poziciya = (x, y + 1)
            self.schetchik_hodov += 1
            return True
        return False
    def proverit_pobedu(self):
        dolzhno_bit = 1
        for i in range(self.razmer):
            for j in range(self.razmer):
                if i == self.razmer - 1 and j == self.razmer - 1:
                    if self.pole[i][j] != 0:
                        return False
                else:
                    if self.pole[i][j] != dolzhno_bit:
                        return False
                    dolzhno_bit += 1
        return True
    def poluchit_pole(self):
        return self.pole
    def poluchit_pustuyu_poziciyu(self):
        return self.pustaya_poziciya
    def poluchit_schetchik_hodov(self):
        return self.schetchik_hodov
    def mozhno_hodit(self, kuda):
        x, y = self.pustaya_poziciya
        if kuda == 'verh' and x > 0:
            return True
        elif kuda == 'niz' and x < self.razmer - 1:
            return True
        elif kuda == 'levo' and y > 0:
            return True
        elif kuda == 'pravo' and y < self.razmer - 1:
            return True

        return False