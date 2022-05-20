'''Крестики-нолики'''
import re
import random
empty_symbol = ' '
x_y =[]


def board_of_play(size):
    board_line = [empty_symbol for i in range(size)]
    board = [board_line.copy() for i in range(size)]
    return board

def draw_board(size, board):
    board_1 = board
    for i in range(size):
        print('-' * (3 * size + (size + 1)))
        for j in range(size):
            print('|', board_1[i][j], end=' ')
        print('|')
    print('-' * (3 * size + (size + 1)))


def win_line(symbol, len_of_line):
    win_line_in_list = [symbol for i in range(int(len_of_line))]
    win_line = re.sub(r"[',[\]]", '', str(win_line_in_list))
    return win_line

def is_win(size, board, x, y, symbol, len_of_line):
    row = []
    for i in range(size):
        row.append(board[int(x)][int(i)])
    row = re.sub(r"[',[\]]", '', str(row))

    column = []
    for i in range(size):
        column.append(board[int(i)][int(y)])
    column = re.sub(r"[',[\]]", '', str(column))

    diag_down = []
    diag_up = []

    for i in range(int(size)):
        for j in range(int(size)):
            if x >= y and (i - j) == (int(x) - int(y)):
                diag_down.append(board[int(i)][int(j)])
            if (i + j) == (int(x) + int(y)):
                diag_up.append(board[int(i)][int(j)])
            if x < y and (j - i) == (int(y) - int(x)):
                diag_down.append(board[int(i)][int(j)])

    diag_down = re.sub(r"[',[\]]", '', str(diag_down))
    diag_up = re.sub(r"[',[\]]", '', str(diag_up))


    if win_line(symbol, len_of_line) in row or win_line(symbol, len_of_line) in column or \
            win_line(symbol, len_of_line) in diag_up or win_line(symbol, len_of_line) in diag_down:
        print('Победа игрока', symbol)
        return True
    else:
        return False

def check_input(x, y, len_of_line, size):
    if str(x).isdigit() and str(y).isdigit() and int(len_of_line) in range(size+1) and int(x) in range(size) and int(y) in range(size):
        return True
    else:
        print('Введенные координаты за пределами поля')
    return False

def cell_is_empty(x, y, board):
    if board[int(x)][int(y)] == empty_symbol:
        return True
    else:
        return False

def board_is_full(size, board):
    count = 0
    for i in range(size):
        for j in range(size):
            if cell_is_empty(i, j, board) == True:
                count +=1
    if count == 0:
        return True
    else:
        return False


def player():
    symbol = input('Введите символ игрока')
    return symbol

def random_player():
    symbol = input('Введите символ игрока')
    return symbol

def count_of_players(player_i, list_of_players):
    list_of_players.append(player_i)
    return list_of_players


def human_player():
    symbol = input('Введите символ игрока')
    return symbol

def move_of_human_player(board, symbol, len_of_line, size):
    x = input('Введите номер строки')
    y = input('Введите номер колонки')
    if check_input(x, y, len_of_line, size) == True:
        while cell_is_empty(x, y, board) == False:
            print('Эта клетка уже занята! Выберите другие координаты')
            x = input('Введите номер строки')
            y = input('Введите номер колонки')
        board[int(x)][int(y)] = symbol
        x_y.append(x)
        x_y.append(y)
    return x_y

def move_of_AI_player(symbol, board, size, len_of_line):
    x, y = random.randint(0, size - 1), random.randint(0, size - 1)

    while cell_is_empty(x, y, board) == False:
        x, y = random.randint(0, size - 1), random.randint(0, size - 1)
    board[int(x)][int(y)] = symbol
    x_y.append(x)
    x_y.append(y)
    return x_y

def check_of_player(symbol, type_of_player, size, board, len_of_line):
    if type_of_player == 1:
        move_of_AI_player(symbol, board, size, len_of_line)

    else:
        move_of_human_player(board, symbol, len_of_line, size)

def play():
    count = 0
    size = int(input('Введите размер игрового поля'))
    board = board_of_play(size)
    list_of_players = []
    list_of_symbol = []
    amount_of_players = int(input('Введите количество игроков'))
    for i in range(1, amount_of_players + 1):
        answer = int(input(f'Кто будет игроком {i} Введите 1, если AI и 0, если человек '))
        if answer == 1:
            list_of_symbol.append(random_player())

            count_of_players(answer, list_of_players)
        else:
            list_of_symbol.append(human_player())
            count_of_players(answer, list_of_players)

    len_of_line = input('Введите длину выигрышной линии')
    while count == 0:
        for i in list_of_symbol:
            print('Ход игрока', i)
            check_of_player(i, list_of_players[list_of_symbol.index(i)], size, board, len_of_line)
            draw_board(size, board)
            if is_win(size, board, x_y[-2], x_y[-1], i, len_of_line):
                count += 1
                draw_board(size, board)
                break
            if board_is_full(size, board) == True:
                count += 1
                print('Ничья!')
                break

play()

