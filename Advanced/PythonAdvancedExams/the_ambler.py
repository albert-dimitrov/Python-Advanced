def check_boundaries(next_row_pos, next_col_pos):
    if 0 <= next_row_pos < n and 0 <= next_col_pos < n:
        return False

    return True

n = int(input())
gambler_coord = []
board = []


gambler_total_amount = 100

moves = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1),
}

for row in range(n):
    line = list(input())
    if 'G' in line:
        position = line.index('G')
        gambler_coord = [row, position]
        line[position] = '-'

    board.append(line)

while True:
    direction = input()

    if direction == 'end':
        print(f'End of the game. Total amount: {gambler_total_amount}$')
        break

    next_row_pos = gambler_coord[0] + moves[direction][0]
    next_col_pos = gambler_coord[1] + moves[direction][1]

    if check_boundaries(next_row_pos, next_col_pos):
        print("Game over! You lost everything!")
        exit(0)

    gambler_coord = [next_row_pos, next_col_pos]

    if board[next_row_pos][next_col_pos] == 'W':
        board[next_row_pos][next_col_pos] = '-'
        gambler_total_amount += 100
    elif board[next_row_pos][next_col_pos] == 'P':
        board[next_row_pos][next_col_pos] = '-'
        gambler_total_amount -= 200
    elif board[next_row_pos][next_col_pos] == 'J':
        board[next_row_pos][next_col_pos] = '-'
        gambler_total_amount += 100000
        print(f"You win the Jackpot!\nEnd of the game. Total amount: {gambler_total_amount}$")
        break

    if gambler_total_amount <= 0:
        print("Game over! You lost everything!")
        exit(0)

board[gambler_coord[0]][gambler_coord[1]] = 'G'

[print(''.join(line)) for line in board]
