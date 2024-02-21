def detonating(matrix, row, col, damage, sides):
    for side in sides:
        if 0 <= row + side[0] < len(matrix) and 0 <= col + side[1] < len(matrix) and matrix[row + side[0]][col + side[1]] > 0:
            matrix[row + side[0]][col + side[1]] -= damage
        else:
            continue
            
    matrix[r][c] = 0

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]
coordinates = tuple(tuple(int(x) for x in cords.split(',')) for cords in input().split())

directions = (
    (-1, 0),
    (1, 0),
    (0, -1),
    (0, 1),
    (-1, -1),
    (-1, 1),
    (1, -1),
    (1, 1)
)

for cord in coordinates:
    r, c = cord[0], cord[1]

    if matrix[r][c] > 0:
        bomb_damage = matrix[r][c]
        detonating(matrix, r, c, bomb_damage, directions)

alive_cells = [x for row in range(len(matrix)) for x in matrix[row] if x > 0]

print(f"Alive cells: {len(alive_cells)}")
print(f"Sum: {sum(alive_cells)}")
[print(*row) for row in matrix]
