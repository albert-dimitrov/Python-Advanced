def is_outside(next_row, next_col):
    if 0 <= next_row < n and 0 <= next_col < m:
        return False

    return True

def check_board(cupboard, mouse_pos, next_row, next_col):
    global total_cheeses

    if cupboard[next_row][next_col] == 'C':
        mouse_pos[0], mouse_pos[1] = next_row, next_col
        cupboard[next_row][next_col] = '*'
        total_cheeses -= 1
    elif cupboard[next_row][next_col] == 'T':
        mouse_pos[0], mouse_pos[1] = next_row, next_col

    elif cupboard[next_row][next_col] == '*':
        mouse_pos[0], mouse_pos[1] = next_row, next_col


n, m = [int(x) for x in input().split(',')]

mouse_pos = []
total_cheeses = 0
cupboard = []

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    line = list(input())

    if 'M' in line:
        mouse_pos = [row, line.index('M')]
        line[line.index('M')] = '*'

    total_cheeses += line.count('C')
    cupboard.append(line)

direction = input()

while direction != "danger":

    next_row, next_col = mouse_pos[0] + moves[direction][0], mouse_pos[1] + moves[direction][1]

    if not is_outside(next_row, next_col):
        check_board(cupboard, mouse_pos, next_row, next_col)

        if total_cheeses == 0:
            print("Happy mouse! All the cheese is eaten, good night!")
            break
        if cupboard[mouse_pos[0]][mouse_pos[1]] == 'T':
            print("Mouse is trapped!")
            break

    else:
        print("No more cheese for tonight!")
        break

    direction = input()
else:
    print("Mouse will come back later!")

cupboard[mouse_pos[0]][mouse_pos[1]] = 'M'

[print(''.join(row)) for row in cupboard]

