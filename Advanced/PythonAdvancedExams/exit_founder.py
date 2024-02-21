def operate(player, row, col, other_player):
    if board[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        exit(0)
    elif board[row][col] == 'T':
        print(f"{player} is out of the game! The winner is {other_player}.")
        exit(0)
    elif board[row][col] == '.':
        return True
    elif board[row][col] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        return False

first_player, second_player = input().split(', ')

board = [[x for x in input().split()] for _ in range(6)]

turn = 0
player_one_skip = False
player_two_skip = False

while True:
    coordinates = input()

    row, col = int(coordinates[1]), int(coordinates[4])
    turn += 1

    if turn % 2 != 0:
        if player_one_skip:
            player_one_skip = False
            continue

        if not operate(first_player, row, col, second_player):
            player_one_skip = True
    else:
        if player_two_skip:
            player_two_skip = False
            continue

        if not operate(second_player, row, col, first_player):
            player_two_skip = True
