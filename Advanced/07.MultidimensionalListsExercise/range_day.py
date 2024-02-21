def move(direction, steps):
    r = player_pos[0] + directions[direction][0] * steps
    c = player_pos[1] + directions[direction][1] * steps

    if not (0 <= r < SIZE and 0 <= c < SIZE):
        return player_pos
    if field[r][c] == 'x':
        return player_pos

    return [r, c]

def shoot(direction):
    r = player_pos[0] + directions[direction][0]
    c = player_pos[1] + directions[direction][1]

    while 0 <= r < SIZE and 0 <= c < SIZE:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]

    return None

SIZE = 5
field = []

targets = 0
targets_hit = 0
targets_hit_pos = []

player_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(SIZE):
    line = input().split()
    field.append(line)

    if 'A' in line:
        player_pos = [row, line.index('A')]

    targets += field[row].count('x')

for _ in range(int(input())):
    command_info = input().split()
    direction = command_info[1]
    if command_info[0] == 'move':
        steps = int(command_info[2])
        player_pos = move(direction, steps)
    elif command_info[0] == 'shoot':
        target_down_pos = shoot(direction)

        if target_down_pos:
            targets_hit_pos.append(target_down_pos)
            targets_hit += 1

        if targets_hit == targets:
            print(f"Training completed! All {targets} targets hit.")
            break
else:
    print(f"Training not completed! {targets - targets_hit} targets left.")

print(*targets_hit_pos, sep='\n')
