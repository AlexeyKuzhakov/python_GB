# Создайте программу для игры в ""Крестики-нолики"".

print("*" * 5, " Игра Крестики-нолики для двух игроков. ", "*" * 5)
def print_board(board):
    print("-" * 13)
    for i in range(3):
        print('|', board[i * 3], '|', board[1 + i * 3], '|', board[2 + i * 3], '|')
        print("-" * 13)


def move_player(sign):
    check = False
    while not check:
        move = input('Введите номер ячейки, куда поставить ' + sign + ': ')
        try:
            move = int(move)
        except:
            print('Некорректный ввод. Вы уверены, что ввели число? Нужно ввести ЧИСЛО, номер ячейки!!!')
        if move >= 1 and move <= 9:
            if str(board[move - 1]) not in 'XO':
                board[move - 1] = sign
                check = True
            else:
                print('Эта ячейка уже занята.')
        else:
            print('Некорректный ввод. Введите число от 1 до 9.')


def control_win(board):
    coordinates = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for item in coordinates:
        if board[item[0]] == board[item[1]] == board[item[2]]:
            return board[item[0]]
    return False


board = range(1, 10)
board = list(map(str, board))

count = 0
win = False
while not win:
    print_board(board)
    if count % 2 == 0:
        move_player('X')
    else:
        sign = 'O'
        move_player(sign)
    count += 1
    if count > 4:
        value = control_win(board)
        if value:
            print(' Ура! Победил: ' + value)
            win = True
    if count == 9 and win == False:
        print('Ничья.')
        break
print_board(board)