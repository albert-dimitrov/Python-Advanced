from collections import deque

names = deque(input().split())
toss = int(input())
current_kid_num = 0

while len(names) > 1:
    current_kid_num += 1
    kid_in_a_row = names.popleft()
    if current_kid_num == toss:
        print(f"Removed {kid_in_a_row}")
        current_kid_num = 0
    else:
        names.append(kid_in_a_row)

print(f"Last is {names.popleft()}")
