rows, columns = [int(x) for x in input().split()]
matrix = [input().split() for _ in range(rows)]
squares_found = 0

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        symbols = {
        matrix[row_index][col_index],
        matrix[row_index][col_index + 1],
        matrix[row_index + 1][col_index],
        matrix[row_index + 1][col_index + 1]
        }
        if len(symbols) == 1:
            squares_found += 1

print(squares_found)
