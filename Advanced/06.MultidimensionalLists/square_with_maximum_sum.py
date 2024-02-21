rows, columns = [int(x) for x in input().split(', ')]
matrix = [[int(x) for x in input().split(', ')] for _ in range(rows)]

submatrix = []
biggest_sum = float('-inf')

for row in range(rows - 1):
    for col in range(columns - 1):

        curr_sum = (matrix[row][col]
                    + matrix[row][col + 1]
                    + matrix[row + 1][col]
                    + matrix[row + 1][col + 1])

        if curr_sum > biggest_sum:
            biggest_sum = curr_sum
            submatrix = [[matrix[row][col], matrix[row][col + 1]], [matrix[row + 1][col], matrix[row + 1][col + 1]]]


print(*submatrix[0])
print(*submatrix[1])
print(biggest_sum)
