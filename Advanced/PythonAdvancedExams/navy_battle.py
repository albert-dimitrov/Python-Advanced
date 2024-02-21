def return_symbol():
    return battlefield[submarine_pos[0]][submarine_pos[1]]


n = int(input())

battlefield = []
submarine_pos = []

times_taken_damage = 0
cruisers_destroyed = 0

for index in range(n):
    line = list(input())

    if 'S' in line:
        submarine_pos = [index, line.index('S')]
        line[line.index('S')] = '-'

    battlefield.append(line)

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

direction = input()

while direction:
    next_row, next_col = submarine_pos[0] + moves[direction][0], submarine_pos[1] + moves[direction][1]

    submarine_pos = [next_row, next_col]

    position = return_symbol()

    if position == '*':
        battlefield[submarine_pos[0]][submarine_pos[1]] = '-'
        times_taken_damage += 1
    elif position == 'C':
        battlefield[submarine_pos[0]][submarine_pos[1]] = '-'
        cruisers_destroyed += 1

    if times_taken_damage == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{', '.join([str(x) for x in submarine_pos])}]!")
        break

    if cruisers_destroyed == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    direction = input()

battlefield[submarine_pos[0]][submarine_pos[1]] = 'S'

[print(''.join(row)) for row in battlefield]
