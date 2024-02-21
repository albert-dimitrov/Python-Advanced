import copy

def extend_liar(copy_matrix):
    for row_index in range(n):
        for col_index in range(m):
            if matrix[row_index][col_index] == 'B':
                for direction in directions:
                    if 0 <= row_index + directions[direction][0] < n\
                        and 0 <= col_index + directions[direction][1] < m\
                        and copy_matrix[row_index +directions[direction][0]][col_index + directions[direction][1]] != 'B':
                        copy_matrix[row_index +directions[direction][0]][col_index + directions[direction][1]] = "B"
                    else:
                        continue

def is_won(matrix, player_pos, move, final_indices):
    if 0 <= player_pos[0] + directions[move][0] < n\
        and 0 <= player_pos[1] + directions[move][1] < m:
        if matrix[player_pos[0] + directions[move][0]][player_pos[1] + directions[move][1]] == 'B':
            return False
        else:
            return None
    else:
        return True

def moving(player_pos, move, final_indices):
    final_indices = [player_pos[0] + directions[move][0], player_pos[1] + directions[move][1]]
    return final_indices

n, m = [int(x) for x in input().split()]
matrix = []
player_pos = []
final_indices = []

for rows_index in range(n):
    row = list(input())

    if 'P' in row:
        cols_index = row.index('P')
        player_pos = [rows_index, cols_index]
        row[cols_index] = '.'

    matrix.append(row)

copy_matrix = copy.deepcopy(matrix)
moves = list(input())

directions = {
    'L': [0, -1],
    'R': [0, 1],
    'U': [-1, 0],
    'D': [1, 0]
}

for move in moves:
    extend_liar(copy_matrix)
    matrix = copy_matrix
    copy_matrix = copy.deepcopy(matrix)

    if is_won(matrix, player_pos, move, final_indices) == True:
        [print(''.join(row)) for row in matrix]
        print(f"won: {player_pos[0]} {player_pos[1]}")
        break
    elif is_won(matrix, player_pos, move, final_indices) == False:
        final_indices = moving(player_pos, move, final_indices)
        [print(''.join(row)) for row in matrix]
        print(f"dead: {final_indices[0]} {final_indices[1]}")
        break
    else:
        player_pos = moving(player_pos, move, final_indices)

