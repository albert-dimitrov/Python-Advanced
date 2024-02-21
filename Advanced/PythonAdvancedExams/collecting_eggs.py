from collections import deque

egg_size = deque([int(x) for x in input().split(', ')])
piece_of_paper_size = deque([int(x) for x in input().split(', ')])

box_filled = 0

while egg_size and piece_of_paper_size:
    egg = egg_size.popleft()

    if egg <= 0:
        continue

    if egg == 13:
        first_paper = piece_of_paper_size.popleft()
        last_paper = piece_of_paper_size.pop()

        piece_of_paper_size.appendleft(last_paper)
        piece_of_paper_size.append(first_paper)

        continue

    paper = piece_of_paper_size.pop()

    total_size = egg + paper

    if total_size <= 50:
        box_filled += 1

if box_filled:
    print(f"Great! You filled {box_filled} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if egg_size:
    print(f'Eggs left: {", ".join([str(x) for x in egg_size])}')

if piece_of_paper_size:
    print(f'Pieces of paper left: {", ".join([str(x) for x in piece_of_paper_size])}')
