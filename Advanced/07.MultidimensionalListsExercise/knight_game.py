def check_knight(pos, moves, matrix):
    total_knights = 0
    for move in moves:
        move_index = [pos[0] + move[0], pos[1] + move[1]]
        if 0 <= move_index[0] < n and 0 <= move_index[1] < n:
            if matrix[move_index[0]][move_index[1]] == "K":
                total_knights += 1
    return total_knights


n = int(input())
board = [list(input()) for _ in range(n)]

knight_moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (-1, 2),
    (1, -2),
    (1, 2),
    (2, -1),
    (2, 1)
)
removed_knights = 0

while True:
    max_attack = 0
    knight_most_attack_pos = []

    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                knight_pos = [row, col]
                attack_count = check_knight(knight_pos, knight_moves, board)

                if attack_count > max_attack:
                    knight_most_attack_pos = [row, col]
                    max_attack = attack_count

    if knight_most_attack_pos:
        r, c = knight_most_attack_pos
        board[r][c] = '0'
        removed_knights += 1
    else:
        break

print(removed_knights)
