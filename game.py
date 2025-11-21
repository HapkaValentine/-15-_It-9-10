import random

class Game15:
    def __init__(self):
        self.size = 4
        self.board = []
        self.empty_pos = (3, 3)
        self.moves_count = 0
        self.reset()

    def reset(self):
        self.board = []
        num = 1
        for i in range(self.size):
            row = []
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    row.append(0)
                else:
                    row.append(num)
                    num += 1
            self.board.append(row)
        
        self.empty_pos = (self.size - 1, self.size - 1)
        self.moves_count = 0

    def shuffle(self, count=1000):
        directions = ['up', 'down', 'left', 'right']
        for _ in range(count):
            direction = random.choice(directions)
            self.move(direction)

    def move(self, direction):
        x, y = self.empty_pos
        new_x, new_y = x, y
        if direction == 'up' and x > 0:
            new_x = x - 1
        elif direction == 'down' and x < self.size - 1:
            new_x = x + 1
        elif direction == 'left' and y > 0:
            new_y = y - 1
        elif direction == 'right' and y < self.size - 1:
            new_y = y + 1
        else:
            return False
        self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
        self.empty_pos = (new_x, new_y)
        self.moves_count += 1
        return True

    def check_win(self):
        expected = 1
        for i in range(self.size):
            for j in range(self.size):
                if i == self.size - 1 and j == self.size - 1:
                    if self.board[i][j] != 0:
                        return False
                else:
                    if self.board[i][j] != expected:
                        return False
                    expected += 1
        return True

    def get_board(self):
        return self.board

    def get_empty_pos(self):
        return self.empty_pos

    def get_moves_count(self):
        return self.moves_count