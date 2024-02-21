n = int(input())

matrix = []
bunny_pos = []
best_path = []

best_direction = None
max_collected_eggs = float('-inf')

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    line = input().split()

    if 'B' in line:
        col = line.index('B')
        bunny_pos = [row, col]

    matrix.append(line)

for direction, position in directions.items():
    row, col = [
        bunny_pos[0] + position[0],
        bunny_pos[1] + position[1]
    ]

    path = []
    collected_eggs = 0

    while 0 <= row < n and 0 <= col < n:
        if matrix[row][col] == 'X':
            break

        collected_eggs += int(matrix[row][col])
        path.append([row, col])

        row += position[0]
        col += position[1]

    if collected_eggs >= max_collected_eggs:
        max_collected_eggs = collected_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep='\n')
print(max_collected_eggs)

