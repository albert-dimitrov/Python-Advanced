def handle_boundaries(next_row_index, next_col_index):
    if next_row_index < 0:
        next_row_index = n - 1
    elif next_row_index == n:
        next_row_index = 0

    if next_col_index < 0:
        next_col_index = n - 1
    elif next_col_index == n:
        next_col_index = 0

    return next_row_index, next_col_index


n = int(input())

fishing_area = []
fisherman_pos = []
quota = 0

whirlpool = False

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for _ in range(n):
    row = list(input())

    if 'S' in row:
        fisherman_pos = [_, row.index('S')]
        row[row.index('S')] = '-'

    fishing_area.append(row)

while True:
    direction = input()

    if direction == 'collect the nets':
        break

    fishing_area[fisherman_pos[0]][fisherman_pos[1]] = '-'

    next_row_index = fisherman_pos[0] + moves[direction][0]
    next_col_index = fisherman_pos[1] + moves[direction][1]

    next_row, next_col = handle_boundaries(next_row_index, next_col_index)
    fisherman_pos = [next_row, next_col]

    if fishing_area[next_row][next_col].isdigit():
        quota += int(fishing_area[next_row][next_col])
    elif fishing_area[next_row][next_col] == 'W':
        whirlpool = True
        quota = 0
        break

    fishing_area[fisherman_pos[0]][fisherman_pos[1]] = 'S'


if whirlpool:
    print(f"You fell into a whirlpool! "
          f"The ship sank and you lost the fish you caught. "
          f"Last coordinates of the ship: [{','.join([str(x) for x in fisherman_pos])}]")
else:
    if quota >= 20:
        print("Success! You managed to reach the quota!")
    else:
        print(f"You didn't catch enough fish and didn't reach the quota! You need {20 - quota} tons of fish more.")

    if quota > 0:
        print(f"Amount of fish caught: {quota} tons.")

    [print(''.join(line)) for line in fishing_area]
