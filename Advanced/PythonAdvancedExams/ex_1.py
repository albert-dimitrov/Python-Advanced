from collections import deque

amount_of_money = [int(x) for x in input().split()]
price_of_foods = deque([int(x) for x in input().split()])

food_count = 0

while amount_of_money and price_of_foods:
    curr_money = amount_of_money.pop()
    curr_food = price_of_foods.popleft()

    if curr_money == curr_food:
        food_count += 1
    elif curr_money > curr_food:
        money_left = curr_money - curr_food
        food_count += 1

        if not amount_of_money:
            amount_of_money.append(money_left)
        else:
            amount_of_money[-1] += money_left

if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif food_count > 1:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print("Henry remained hungry. He will try next weekend again.")
