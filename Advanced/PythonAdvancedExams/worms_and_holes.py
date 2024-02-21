from collections import deque

worms = [int(x) for x in input().split()]
holes = deque(int(x) for x in input().split())

worm_count = len(worms)
matches = 0

while True:
    if not holes:
        break

    if not worms:
        break

    worm = worms.pop()
    hole = holes.popleft()

    if worm == hole:
        matches += 1
    else:
        worm -= 3

        if worm > 0:
            worms.append(worm)

if matches > 0:
    print(f"Matches: {matches}")
else:
    print("There are no matches.")

if not worms and matches == worm_count:
    print("Every worm found a suitable hole!")
elif not worms and matches < worm_count:
    print("Worms left: none")
elif worms:
    print(f"Worms left: {', '.join([str(x) for x in worms])}")

if holes:
    print(f"Holes left: {', '.join([str(x) for x in holes])}")
else:
    print("Holes left: none")
