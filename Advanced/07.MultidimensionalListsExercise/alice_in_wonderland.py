n = int(input())

matrix = []
alice_pos = []

tea_bags = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    line = input().split()
    matrix.append(line)

    if 'A' in line:
        alice_pos = [row, line.index('A')]
        matrix[row][alice_pos[1]] = '*'

while tea_bags < 10:
    direction = input()

    row = alice_pos[0] + directions[direction][0]
    col = alice_pos[1] + directions[direction][1]

    if not (0 <= row < n and 0 <= col < n):
        break

    alice_pos = [row, col]
    element = matrix[row][col]
    matrix[row][col] = '*'

    if element == 'R':
        break
    elif element.isdigit():
        tea_bags += int(element)

if tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

[print(*row) for row in matrix]
