def is_coordinate_valid(row, col):
    if 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        return True
    return False

n = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(n)]

while True:
    operation = input()
    if 'END' in operation:
        break
    command, row, col, value = operation.split()
    row, col, value = int(row), int(col), int(value)
    if command == 'Add':
        if is_coordinate_valid(row, col):
            matrix[row][col] += value
        else:
            print("Invalid coordinates")
    elif command == 'Subtract':
        if is_coordinate_valid(row, col):
            matrix[row][col] -= value
        else:
            print("Invalid coordinates")

[print(*row) for row in matrix]
