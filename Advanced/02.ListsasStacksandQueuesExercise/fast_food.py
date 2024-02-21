from collections import deque

quantity_of_food = int(input())

clients = deque([int(x) for x in input().split()])
print(max(clients))

while clients:
    current_client = clients.popleft()
    if quantity_of_food - current_client < 0:
        clients.appendleft(current_client)
        break
    else:
        quantity_of_food -= current_client

if clients:
    print("Orders left:", *clients)
else:
    print('Orders complete')
