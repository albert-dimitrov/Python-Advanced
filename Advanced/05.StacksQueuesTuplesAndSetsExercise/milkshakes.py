from collections import deque

chocolates = deque([int(x) for x in input().split(', ')])
cups_of_milk = deque([int(x) for x in input().split(', ')])
prepared_milkshakes = 0

while chocolates and cups_of_milk:
    last_chocolate = chocolates.pop()
    first_cup = cups_of_milk.popleft()

    if first_cup > 0 and last_chocolate > 0:
        if last_chocolate == first_cup:
            prepared_milkshakes += 1
            if prepared_milkshakes == 5:
                print("Great! You made all the chocolate milkshakes needed!")
                break
        else:
            cups_of_milk.append(first_cup)
            last_chocolate -= 5
            if last_chocolate > 0:
                chocolates.append(last_chocolate)
    else:
        if first_cup > 0:
            cups_of_milk.appendleft(first_cup)
        elif last_chocolate > 0:
            chocolates.append(last_chocolate)
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate:", ', '.join([str(x) for x in chocolates]))
else:
    print("Chocolate: empty")

if cups_of_milk:
    print(f"Milk:", ', '.join([str(x) for x in cups_of_milk]))
else:
    print("Milk: empty")