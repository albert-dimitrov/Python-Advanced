def create(start_pos, direction, value):
    next_row, next_col = start_pos[0] + moves[direction][0], start_pos[1] + moves[direction][1]

    if field[next_row][next_col] == '.':
        field[next_row][next_col] = value

    start_pos[0], start_pos[1] = next_row, next_col


def update(start_pos, direction, value):
    next_row, next_col = start_pos[0] + moves[direction][0], start_pos[1] + moves[direction][1]

    if field[next_row][next_col] != '.':
        field[next_row][next_col] = value

    start_pos[0], start_pos[1] = next_row, next_col


def delete(start_pos, direction):
    next_row, next_col = start_pos[0] + moves[direction][0], start_pos[1] + moves[direction][1]

    if field[next_row][next_col] != '.':
        field[next_row][next_col] = '.'

    start_pos[0], start_pos[1] = next_row, next_col


def read(start_pos, direction):
    next_row, next_col = start_pos[0] + moves[direction][0], start_pos[1] + moves[direction][1]

    if field[next_row][next_col] != '.':
        print(field[next_row][next_col])

    start_pos[0], start_pos[1] = next_row, next_col


field = [[x for x in input().split()] for _ in range(6)]

start = input()

first_row, first_col = start[1], start[4]
start_pos = [int(first_row), int(first_col)]

command = input()

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

while command != 'Stop':
    opeartion, *dirvalue = command.split(', ')

    if opeartion == 'Create':
        direction, value = dirvalue[0], dirvalue[1]
        create(start_pos, direction, value)
    elif opeartion == 'Update':
        direction, value = dirvalue[0], dirvalue[1]
        update(start_pos, direction, value)
    elif opeartion == 'Delete':
        direction = dirvalue[0]
        delete(start_pos, direction)
    elif opeartion == 'Read':
        direction = dirvalue[0]
        read(start_pos, direction)

    command = input()

[print(' '.join(row)) for row in field]
