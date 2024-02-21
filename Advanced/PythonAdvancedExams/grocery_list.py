def shop_from_grocery_list(budget, grocery_list, *args):
    purchased_grocery = []

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    for product, price in args:
        if product not in grocery_list or product in purchased_grocery:
            continue

        if price > budget:
            break

        purchased_grocery.append(product)
        budget -= price
        grocery_list.remove(product)

    if not grocery_list:
        return f"Shopping is successful. Remaining budget: {budget:.2f}."

    return f"You did not buy all the products. Missing products: {', '.join(grocery_list)}."


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
