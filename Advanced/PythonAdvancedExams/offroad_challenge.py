from collections import deque

fuel = [int(x) for x in input().split()]
consumption_index = deque([int(x) for x in input().split()])
quantities_of_fuel_needed = deque([int(x) for x in input().split()])

reached_altitude = []
reached_altitude_number = 0
finished = False

while fuel:
    fuel_quantity = fuel.pop()
    current_consumption = consumption_index.popleft()

    result = fuel_quantity - current_consumption

    if result >= quantities_of_fuel_needed.popleft():
        reached_altitude_number += 1
        reached_altitude.append(f'Altitude {reached_altitude_number}')
        print(f"John has reached: Altitude {reached_altitude_number}")
    else:
        print(f"John did not reach: Altitude {reached_altitude_number + 1}")
        break

    if not quantities_of_fuel_needed:
        finished = True
        break

if reached_altitude_number > 0:
    if not finished:
        print(f"John failed to reach the top.\nReached altitudes: {', '.join(reached_altitude)}")
    else:
        print("John has reached all the altitudes and managed to reach the top!")
else:
    print("John failed to reach the top.\nJohn didn't reach any altitude.")

