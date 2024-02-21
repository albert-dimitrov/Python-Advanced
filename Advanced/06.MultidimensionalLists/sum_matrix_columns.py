rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

for col in range(columns):
    sum = 0
    for row in range(rows):
        sum += matrix[row][col]
    print(sum)
