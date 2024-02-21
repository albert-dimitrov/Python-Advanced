def moving_santa(santa_pos, neighborhood):
    r, c = santa_pos

    if neighborhood[r][c] == 'V':
        return 'V'
    elif neighborhood[r][c] == 'X':
        return 'X'
    elif neighborhood[r][c] == 'C':
        return 'C'

    return '-'

def step_on_cookie(neighborhood, number_of_presents, nice_kids_count, directions):
    for direction in directions.values():
        r = santa_pos[0] + direction[0]
        c = santa_pos[1] + direction[1]

        if 0 <= r < n and 0 <= c < n:
            if neighborhood[r][c] == 'V':
                number_of_presents -= 1
                nice_kids_count += 1
            elif neighborhood[r][c] == 'X':
                number_of_presents -= 1

            neighborhood[r][c] = '-'
            if number_of_presents == 0:
                return [number_of_presents, nice_kids_count]

    return [number_of_presents, nice_kids_count]





number_of_presents = int(input())
n = int(input())

neighborhood = []
santa_pos = []
total_nice_kids_count = 0
nice_kids_count = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(n):
    line = input().split()
    neighborhood.append(line)

    if 'S' in line:
        santa_pos = [row, line.index('S')]
        neighborhood[row][santa_pos[1]] = '-'
    total_nice_kids_count += line.count('V')


while number_of_presents > 0:
    command = input()

    if command == 'Christmas morning':
        break

    r = santa_pos[0] + directions[command][0]
    c = santa_pos[1] + directions[command][1]

    if 0 <= r < n and 0 <= c < n:
        santa_pos = [r, c]
        cell_type = moving_santa(santa_pos, neighborhood)

        if cell_type == 'V':
            neighborhood[santa_pos[0]][santa_pos[1]] = '-'
            number_of_presents -= 1
            nice_kids_count += 1
        elif cell_type == 'X':
            neighborhood[santa_pos[0]][santa_pos[1]] = '-'
        elif cell_type == 'C':
            neighborhood[santa_pos[0]][santa_pos[1]] = '-'
            number_of_presents, nice_kids_count = step_on_cookie(neighborhood, number_of_presents, nice_kids_count, directions)

else:
    if total_nice_kids_count > nice_kids_count:
        print("Santa ran out of presents!")

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'
[print(*row) for row in neighborhood]

if total_nice_kids_count == nice_kids_count:
    print(f"Good job, Santa! {total_nice_kids_count} happy nice kid/s.")
else:
    print(f"No presents for {total_nice_kids_count - nice_kids_count} nice kid/s.")
