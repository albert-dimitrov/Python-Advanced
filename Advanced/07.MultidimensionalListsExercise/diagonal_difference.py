rows = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

primary_diagonal = []
secondary_diagonal = []

for index in range(rows):
    primary_diagonal.append(matrix[index][index])
    secondary_diagonal.append(matrix[index][rows - index - 1])

print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))
