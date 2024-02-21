from collections import deque

def out_of_field(squirrel_pos):
    if 0 <= squirrel_pos[0] < n and 0 <= squirrel_pos[1] < n:
        return False

    return True

def check_position(squirrel_pos, field):
    return field[squirrel_pos[0]][squirrel_pos[1]]


n = int(input())

collected_hazelnuts = 0
squirrel_pos = []

moves = deque(input().split(', '))
field = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for row in range(n):
    line = list(input())

    if 's' in line:
        squirrel_pos = [row, line.index('s')]

    field.append(line)

while moves:
    current_move = moves.popleft()

    squirrel_pos = [squirrel_pos[0] + directions[current_move][0], squirrel_pos[1] + directions[current_move][1]]

    if not out_of_field(squirrel_pos):
        position = check_position(squirrel_pos, field)

        if position == 'h':
            field[squirrel_pos[0]][squirrel_pos[1]] = '*'
            collected_hazelnuts += 1

            if collected_hazelnuts == 3:
                print("Good job! You have collected all hazelnuts!")
                break
        elif position == 't':
            print("Unfortunately, the squirrel stepped on a trap...")
            break
        else:
            continue

    else:
        print("The squirrel is out of the field.")
        break

else:
    print("There are more hazelnuts to collect.")

print(f"Hazelnuts collected: {collected_hazelnuts}")
