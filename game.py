import random

class Game15:
    def __init__(self):
        self.size = 4
        self.board = []
        self.empty = (3, 3)
        self.moves = 0
        self.start()
    def start(self):
        self.board = []
        n = 1
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    row.append(0)
                else:
                    row.append(n)
                    n += 1
            self.board.append(row)
        self.empty = (self.size - 1, self.size - 1)
        self.moves = 0
    def peremeshat(self, k=1000):
        dirs = ['verh', 'niz', 'levo', 'pravo']
        for _ in range(k):
            d = random.choice(dirs)
            self.hodit(d)
    def hodit(self, d):
        x, y = self.empty
        if d == 'verh' and x > 0:
            self.board[x][y], self.board[x - 1][y] = self.board[x - 1][y], self.board[x][y]
            self.empty = (x - 1, y)
            self.moves += 1
            return True
        if d == 'niz' and x < self.size - 1:
            self.board[x][y], self.board[x + 1][y] = self.board[x + 1][y], self.board[x][y]
            self.empty = (x + 1, y)
            self.moves += 1
            return True
        if d == 'levo' and y > 0:
            self.board[x][y], self.board[x][y - 1] = self.board[x][y - 1], self.board[x][y]
            self.empty = (x, y - 1)
            self.moves += 1
            return True
        if d == 'pravo' and y < self.size - 1:
            self.board[x][y], self.board[x][y + 1] = self.board[x][y + 1], self.board[x][y]
            self.empty = (x, y + 1)
            self.moves += 1
            return True
        return False
    def proverit_pobedu(self):
        need = 1
        for i in range(self.size):
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    if self.board[i][j] != 0:
                        return False
                else:
                    if self.board[i][j] != need:
                        return False
                    need += 1
        return True
    def poluchit_pole(self):
        return self.board
    def poluchit_pustuyu_poziciyu(self):
        return self.empty
    def poluchit_schetchik_hodov(self):
        return self.moves
    def mozhno_hodit(self, d):
        x, y = self.empty
        if d == 'verh' and x > 0:
            return True
        if d == 'niz' and x < self.size - 1:
            return True
        if d == 'levo' and y > 0:
            return True
        if d == 'pravo' and y < self.size - 1:
            return True
        return False
