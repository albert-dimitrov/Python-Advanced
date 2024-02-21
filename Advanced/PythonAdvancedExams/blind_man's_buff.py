def check_move(row, col):
    if 0 <= row < n and 0 <= col < m:
        if playground[row][col] != 'O':
            return True

    return False

n, m = [int(x) for x in input().split()]

playground = []
my_pos = []

for row_index in range(n):
    line = input().split()

    if 'B' in line:
        my_pos = [row_index, line.index('B')]

    playground.append(line)

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

moves_made = 0
count_of_touched_people = 0

direction = input()
while direction != 'Finish':
    next_row, next_col = my_pos[0] + moves[direction][0], my_pos[1] + moves[direction][1]

    if count_of_touched_people == 3:
        break

    if check_move(next_row, next_col):
        my_pos = [next_row, next_col]
        moves_made += 1

        if playground[my_pos[0]][my_pos[1]] == 'P':
            count_of_touched_people += 1
            playground[my_pos[0]][my_pos[1]] = '-'

    direction = input()

print('Game over!')
print(f"Touched opponents: {count_of_touched_people} Moves made: {moves_made}")

