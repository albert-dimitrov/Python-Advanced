n = int(input())

jet_fighter_pos = []
jet_armor = 300
enemy_jet_count = 4

air_space = []

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}


for row_index in range(n):
    line = list(input())

    if 'J' in line:
        jet_fighter_pos = [row_index, line.index('J')]
        line[line.index('J')] = '-'

    air_space.append(line)

while True:
    direction = input()

    next_row, next_col = jet_fighter_pos[0] + moves[direction][0], jet_fighter_pos[1] + moves[direction][1]
    jet_fighter_pos = [next_row, next_col]

    if air_space[next_row][next_col] == '-':
        continue
    elif air_space[next_row][next_col] == 'E':
        if enemy_jet_count > 1:
            jet_armor -= 100
            enemy_jet_count -= 1

            if jet_armor == 0:
                print(f"Mission failed, your jetfighter was shot down! Last coordinates [{next_row}, {next_col}]!")
                air_space[next_row][next_col] = 'J'
                break

            air_space[next_row][next_col] = '-'
        elif enemy_jet_count == 1:
            air_space[next_row][next_col] = 'J'
            print("Mission accomplished, you neutralized the aerial threat!")
            break
    elif air_space[next_row][next_col] == 'R':
        air_space[next_row][next_col] = '-'
        jet_armor = 300

[print(''.join(row)) for row in air_space]
