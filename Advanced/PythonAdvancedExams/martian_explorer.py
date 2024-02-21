from collections import deque


def check_field(next_row, next_col):
    if 0 <= next_row < 6 and 0 <= next_col < 6:
        return True

    return False


def fix_position(next_row, next_col):
    if next_row < 0:
        next_row = 5
    elif next_row == 6:
        next_row = 0
    elif next_col < 0:
        next_col = 5
    elif next_col == 6:
        next_col = 0

    return next_row, next_col


rover_pos = []

field = []

for row_index in range(6):
    line = input().split()

    if 'E' in line:
        rover_pos = [row_index, line.index('E')]

    field.append(line)

directions = deque(input().split(', '))

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

deposits = {
    'W': 'Water',
    "M": 'Metal',
    'C': 'Concrete',
}

found_deposits = set()

while directions:
    direction = directions.popleft()

    next_row, next_col = rover_pos[0] + moves[direction][0], rover_pos[1] + moves[direction][1]

    if not check_field(next_row, next_col):
        next_row, next_col = fix_position(next_row, next_col)

    rover_pos = [next_row, next_col]

    if field[rover_pos[0]][rover_pos[1]] == "W"\
        or field[rover_pos[0]][rover_pos[1]] == 'M'\
        or field[rover_pos[0]][rover_pos[1]] == 'C':

        print(f"{deposits[field[rover_pos[0]][rover_pos[1]]]} deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        found_deposits.add(field[rover_pos[0]][rover_pos[1]])
    elif field[rover_pos[0]][rover_pos[1]] == 'R':
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break

if len(found_deposits) == 3:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
