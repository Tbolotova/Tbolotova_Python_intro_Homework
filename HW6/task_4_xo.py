from random import *


def check_win(current_field, win_size, current_symbol):
    is_win = (check_vertical_horizontal(current_field, win_size, current_symbol)
              or check_diagonals(current_field, win_size, current_symbol))
    return is_win


def check_vertical_horizontal(current_field, win_size, current_symbol):
    verticals_and_horizontals = ([[[i, j] for i in range(len(current_field))] for j in range(len(current_field))]
                                 + [[[j, i] for i in range(len(current_field))] for j in range(len(current_field))])
    count_sym = 0
    for i in range(len(verticals_and_horizontals)):
        for j in verticals_and_horizontals[i]:
            if current_field[j[0]][j[1]] == current_symbol:
                count_sym += 1
            else:
                count_sym = 0
        if count_sym == win_size:
            return True
    return False


def check_diagonals(current_field, check_size, current_symbol):
    count_win = 0
    for offset in range(len(current_field) - check_size + 1):
        for i in range(len(current_field) - offset):
            if current_field[i][i + offset] == current_symbol:
                count_win += 1
            else:
                count_win = 0
            if count_win == check_size:
                return True
        for i in range(len(current_field) - offset):
            if current_field[i + offset][i] == current_symbol:
                count_win += 1
            else:
                count_win = 0
            if count_win == check_size:
                return True
        for i in range(len(current_field) - offset):
            if current_field[len(current_field) - i - 1][i + offset] == current_symbol:
                count_win += 1
            else:
                count_win = 0
            if count_win == check_size:
                return True
        for i in range(len(current_field) - offset):
            if current_field[len(current_field) - i - 1 - offset][i] == current_symbol:
                count_win += 1
            else:
                count_win = 0
            if count_win == check_size:
                return True
    return False


def print_field(current_field):
    for i in range(len(current_field)):
        for j in range(len(current_field[i])):
            print(f"|{f'{current_field[i][j]}':^3}", end='')
        print("|")


# TODO: make the AI smart
def ai_turn(current_field, current_symbol, win_size):
    is_valid = False
    ai_coordinates = []
    while not is_valid:
        ai_coordinates = [randint(0, len(current_field) - 1) for _ in range(2)]
        is_valid = is_coordinates_valid(ai_coordinates, current_field)
    print(f"The AI set its symbol to coordinates: [{ai_coordinates[0] + 1}, {ai_coordinates[1] + 1}].")
    return ai_coordinates


def player_turn(current_field):
    is_valid = False
    player_coordinates = []
    while not is_valid:
        try:
            player_coordinates = [int(input("Please enter the vertical coordinate for your turn: ")) - 1,
                                  int(input("Please enter the horizontal coordinate for your turn: ")) - 1]
        except ValueError:
            print("The coordinates you have entered are not valid. Please enter new coordinates. ")
            continue
        is_valid = is_coordinates_valid(player_coordinates, current_field)
        if not is_valid:
            print("The coordinates you have entered are not valid. Please enter new coordinates. ")
    print(f"You set your symbol to coordinates: [{player_coordinates[0] + 1}, {player_coordinates[1] + 1}].")
    return player_coordinates


def is_coordinates_valid(coordinates, current_field):
    if coordinates[0] >= len(current_field) or coordinates[1] >= len(current_field):
        return False
    if current_field[coordinates[0]][coordinates[1]] == '':
        return True
    return False


def is_field_full(current_field):
    for i in current_field:
        for j in i:
            if j == '':
                return False
    return True


def set_symbol_to_coordinates(current_field, coordinates, current_symbol):
    current_field[coordinates[0]][coordinates[1]] = current_symbol


def play(field_size, win_size, ai_symbol, player_symbol, current_turn):
    field = [['' for _ in range(field_size)] for _ in range(field_size)]
    print_field(field)
    while not is_field_full(field):
        if current_turn == 'ai':
            set_symbol_to_coordinates(field, ai_turn(field, ai_symbol, win_size), ai_symbol)
            print_field(field)
            if check_win(field, win_size, ai_symbol):
                return current_turn
            current_turn = 'player'
        if current_turn == 'player':
            set_symbol_to_coordinates(field, player_turn(field), player_symbol)
            print_field(field)
            if check_win(field, win_size, player_symbol):
                return current_turn
            current_turn = 'ai'
    return "tie"


print("Let's play tic-tac-toe!")
field_size_input = int(input("Please enter the size of the field you want to play on: "))
win_line_size = int(input("Please enter the size of the winning line: "))
first_turn = choice(['ai', 'player'])
if first_turn == 'ai':
    ai_sym = 'X'
    player_sym = 'O'
    print("The AI will play with X's and will go first! You will play with O's")
else:
    ai_sym = 'O'
    player_sym = 'X'
    print("You will play with X's and will go first! The AI will play with O's")

winner = play(field_size_input, win_line_size, ai_sym, player_sym, first_turn)

if winner == 'ai':
    print("Sorry, the AI won! Try again!")
elif winner == 'player':
    print("Congratulations! You've won!")
else:
    print("The field is full! It's a tie!")
