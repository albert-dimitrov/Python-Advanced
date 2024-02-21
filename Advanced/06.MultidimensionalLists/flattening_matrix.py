rows = int(input())
matrix = []

for row in range(rows):
    line = [int(x) for x in input().split(', ')]
    matrix.append(line)

matrix = [num for row in matrix for num in row]

print(matrix)

# matrix = [[int(x) for x in input().split(', ')] for _ in range(int(input()))]
# print([num for row in matrix for num in row])
