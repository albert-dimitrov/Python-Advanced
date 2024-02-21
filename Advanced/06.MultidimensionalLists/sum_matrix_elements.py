rows, columns = [int(x) for x in input().split(', ')]
matrix = []
sums = 0

for row in range(rows):
    lines = [int(x) for x in input().split(', ')]
    matrix.append(lines)

for index in range(len(matrix)):
    sums += sum(matrix[index])

print(sums)
print(matrix)