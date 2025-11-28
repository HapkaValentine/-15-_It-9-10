
from random import shuffle
p = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9,10,11,12],
     [13,14,15,0]]
numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
shuffle(numbers)
k = 0
for i in range(4):
    for j in range(4):
        p[i][j] = numbers[k]
        k = k + 1
print("Привет! Это пятнашки")
print("Двигай пустую клетку клавишами: w s a d или ц ы ф в")
print("Чтобы выйти — напиши 'выход'\n")
hodov = 0
while True:
    print("+---------------------+")
    for i in range(4):
        print("|", end="")
        for j in range(4):
            if p[i][j] == 0:
                print("   ", end="")
            elif p[i][j] < 10:
                print(" " + str(p[i][j]) + " ", end="")
            else:
                print(" " + str(p[i][j]), end=" ")
            print("|", end="")
        print()
    print("+---------------------+")
    print("Ходов:", hodov)
    print()
    if p == [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]:
        print("ТЫ ПОБЕДИЛ!!! За", hodov, "ходов!")
        break
    x = input("Твой ход: ")
    if x == "выход" or x == "exit":
        print("Ладно, пока!")
        break
    px = 0
    py = 0
    for i in range(4):
        for j in range(4):
            if p[i][j] == 0:
                px = i
                py = j
    moved = False
    if x in "wц" and px > 0:
        p[px][py], p[px-1][py] = p[px-1][py], p[px][py]
        moved = True
    if x in "sы" and px < 3:
        p[px][py], p[px+1][py] = p[px+1][py], p[px][py]
        moved = True
    if x in "aф" and py > 0:
        p[px][py], p[px][py-1] = p[px][py-1], p[px][py]
        moved = True
    if x in "dв" and py < 3:
        p[px][py], p[px][py+1] = p[px][py+1], p[px][py]
        moved = True
    if moved:
        hodov = hodov + 1
    else:
        print("Сюда нельзя, попробуй ещё раз")
        input("Нажми Enter")
    print("\n" * 2)