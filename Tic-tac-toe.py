def greet():
    print('      --------------')
    print('     Добро пожаловать')
    print('       В крестики')
    print('         нолики')
    print('      --------------')
    print('Координата сосоит из 2 чисел')
    print(' по ветрикали и горизонтали')
    print('Для ввода числа нажми Enter')
    print()


def network():
    print('  | 0 | 1 | 2 |')
    for i, j in enumerate(_str_):
        j_row = f'{i} | {" | ".join(j)} | '
        print('  -------------')
        print(j_row)


def _input_():
    while True:

        x = input('Координата по вертикали : ')
        y = input('Координата по горизонтали: ')

        if not (x.isdigit()) or not (y.isdigit()):
            print()
            print('Кордината не является числом')
            print()
            continue

        x, y = int(x), int(y)

        if x < 0 or x > 2 or y < 0 or y > 2:
            print()
            print('Координата не входит в диапозон')
            print()
            continue

        if _str_[x][y] != ' ':
            print()
            print('Клетка занята')
            print()
            continue

        return x, y


def win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(_str_[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False


def motion():
    if count % 2 != 0:
        print()
        print('Ходит X')
        print()
    else:
        print()
        print('Ходит O')
        print()


greet()
_str_ = [[' '] * 3 for i in range(3)]
network()
print()
count = 0
while True:
    count += 1
    motion()
    x1, y1 = _input_()
    if count % 2 != 0:
        _str_[x1][y1] = 'X'
    else:
        _str_[x1][y1] = 'O'
    print()
    network()
    if win():
        break
    if count == 9:
        print('Ничья')
        break
