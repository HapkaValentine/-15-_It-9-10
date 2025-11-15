import random

class Game15:
    def __init__(self):
        self.razmer = 4
        self.pole = [[0 for _ in range(4)] for _ in range(4)]
        self.pustaya_poziciya = (3, 3)
        self.schetchik_hodov = 0
        self.nachalo()
    def nachalo(self):
        k = 1
        for r in range(self.razmer):
            for c in range(self.razmer):
                if r == self.razmer - 1 and c == self.razmer - 1:
                    self.pole[r][c] = 0
                else:
                    self.pole[r][c] = k
                    k += 1
        self.pustaya_poziciya = (3, 3)
        self.schetchik_hodov = 0
    def peremeshat(self, skolko=1000):
        vec = ["verh", "niz", "levo", "pravo"]
        for i in range(skolko):
            sl = random.randint(0, 3)
            self.hodit(vec[sl])
    def hodit(self, kuda):
        x, y = self.pustaya_poziciya
        nx, ny = x, y
        if kuda == "verh":
            nx = x - 1
        elif kuda == "niz":
            nx = x + 1
        elif kuda == "levo":
            ny = y - 1
        elif kuda == "pravo":
            ny = y + 1
        if 0 <= nx < self.razmer and 0 <= ny < self.razmer:
            self.pole[x][y], self.pole[nx][ny] = self.pole[nx][ny], self.pole[x][y]
            self.pustaya_poziciya = (nx, ny)
            self.schetchik_hodov += 1
            return True
        return False
    def proverit_pobedu(self):
        t = 1
        for r in range(self.razmer):
            for c in range(self.razmer):
                if r == self.razmer - 1 and c == self.razmer - 1:
                    if self.pole[r][c] != 0:
                        return False
                else:
                    if self.pole[r][c] != t:
                        return False
                    t += 1
        return True
    def poluchit_pole(self):
        return self.pole
    def poluchit_pustuyu_poziciyu(self):
        return self.pustaya_poziciya
    def poluchit_schetchik_hodov(self):
        return self.schetchik_hodov
    def mozhno_hodit(self, kuda):
        x, y = self.pustaya_poziciya
        if kuda == "verh":
            return x > 0
        if kuda == "niz":
            return x < self.razmer - 1
        if kuda == "levo":
            return y > 0
        if kuda == "pravo":
            return y < self.razmer - 1
        return False
