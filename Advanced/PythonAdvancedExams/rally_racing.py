n = int(input())
racing_number = input()

car_pos = [0, 0]

tunnels = []
track = []

for row_index in range(n):
    line = input().split()

    if 'T' in line:
        tunnels.append([row_index, line.index('T')])

    track.append(line)

kilometers_passed = 0

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

direction = input()

while direction != 'End':
    next_row, next_col = car_pos[0] + moves[direction][0], car_pos[1] + moves[direction][1]

    if track[next_row][next_col] == 'T':
        kilometers_passed += 30
        track[next_row][next_col] = '.'

        if next_row == tunnels[0][0] and next_col == tunnels[0][1]:
            next_row, next_col = tunnels[1][0], tunnels[1][1]
        else:
            next_row, next_col = tunnels[0][0], tunnels[0][1]

        track[next_row][next_col] = '.'
    elif track[next_row][next_col] == 'F':
        track[next_row][next_col] = 'C'
        print(f"Racing car {racing_number} finished the stage!")
        kilometers_passed += 10
        break
    else:
        kilometers_passed += 10

    car_pos = [next_row, next_col]

    direction = input()

else:
    print(f"Racing car {racing_number} DNF.")
    track[car_pos[0]][car_pos[1]] = 'C'

print(f"Distance covered {kilometers_passed} km.")
[print(''.join(row)) for row in track]
