def finding_target(matrix, target):
    for row in range(len(matrix)):
        for index in range(len(matrix[row])):
            if matrix[row][index] == target:
                return f"({row}, {index})"

    return f"{target} does not occur in the matrix"

rows = int(input())
matrix = [[x for x in input()] for _ in range(rows)]
target = input()

print(finding_target(matrix, target))
