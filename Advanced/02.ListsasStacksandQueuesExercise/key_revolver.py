from collections import deque

price_of_bullet = int(input())
size_of_magazine = int(input())
bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])
intelligence = int(input())
barrel_count = size_of_magazine
bullet_fee = 0

while locks:
    current_lock = locks.popleft()
    current_bullet = bullets.pop()

    if current_bullet <= current_lock:
        print("Bang!")
    else:
        locks.appendleft(current_lock)
        print('Ping!')

    barrel_count -= 1
    bullet_fee += price_of_bullet

    if barrel_count == 0 and bullets:
        print("Reloading!")
        barrel_count = size_of_magazine

    if not bullets:
        break

if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    print(f"{len(bullets)} bullets left. Earned ${intelligence - bullet_fee}")
