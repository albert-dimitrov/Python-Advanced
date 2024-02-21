def check_validation(next_row, next_col):
    if 0 <= next_row < n and 0 <= next_col < m:
        return True
    return False

def check_next_move(next_row, next_col):
    if neighborhood[next_row][next_col] != '*':
        return True

    return False

n, m = [int(x) for x in input().split()]
neighborhood = []
delivery_boy_pos = []
boy_start = []

for row in range(n):
    line = list(input())

    if 'B' in line:
        delivery_boy_pos = [row, line.index('B')]
        boy_start = [row, line.index('B')]

    neighborhood.append(line)

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

direction = input()
while direction:
    next_row = delivery_boy_pos[0] + moves[direction][0]
    next_col = delivery_boy_pos[1] + moves[direction][1]

    if not check_validation(next_row, next_col):
        print("The delivery is late. Order is canceled.")
        neighborhood[boy_start[0]][boy_start[1]] = ' '
        break

    if check_next_move(next_row, next_col):
        if neighborhood[next_row][next_col] == 'P':
            neighborhood[next_row][next_col] = 'R'
            print("Pizza is collected. 10 minutes for delivery.")
        elif neighborhood[next_row][next_col] == 'A':
            neighborhood[next_row][next_col] = 'P'
            print("Pizza is delivered on time! Next order...")
            break
        elif neighborhood[next_row][next_col] == '-':
            neighborhood[next_row][next_col] = '.'

        delivery_boy_pos = [next_row, next_col]



    direction = input()

[print("".join(rows)) for rows in neighborhood]

