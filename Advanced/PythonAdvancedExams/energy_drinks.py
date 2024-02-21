from collections import deque

mg_of_caffeine = [int(x) for x in input().split(', ')]
energy_drinks = deque([int(x) for x in input().split(', ')])

maximum_caffeine = 300
total_caffeine = 0
stamat_caffeine_take = 0

while mg_of_caffeine and energy_drinks:
    maximum_caffeine = 300 - stamat_caffeine_take
    caffeine = mg_of_caffeine.pop()
    drink = energy_drinks.popleft()

    current_caffeine = caffeine * drink

    if current_caffeine <= maximum_caffeine:
        total_caffeine += current_caffeine
        stamat_caffeine_take += current_caffeine
    else:
        energy_drinks.append(drink)
        stamat_caffeine_take -= 30

    if stamat_caffeine_take < 0:
        stamat_caffeine_take = 0

if energy_drinks:
    print(f"Drinks left: {', '.join([str(x) for x in energy_drinks])}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {stamat_caffeine_take} mg caffeine.")
