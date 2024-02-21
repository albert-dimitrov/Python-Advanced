def shopping_cart(*args):
    meal_data = {
        'Soup': [],
        'Pizza': [],
        'Dessert': []
    }

    total_soups = 0
    total_pizza = 0
    total_desert = 0
    added_product = 0

    result = ''

    for element in args:
        if element == 'Stop':
            break

        meal, product = element[0], element[1]

        if product not in meal_data[meal]:

            if meal == 'Soup':
                total_soups += 1

                if total_soups > 3:
                    continue

            elif meal == 'Pizza':
                total_pizza += 1

                if total_pizza > 4:
                    continue

            elif meal == 'Dessert':
                total_desert += 1

                if total_desert > 2:
                    continue

            meal_data[meal].append(product)
            added_product += 1

    if not added_product:
        return "No products in the cart!"

    sorted_meals = sorted(meal_data.items(), key=lambda x: (-len(x[1]), x[0]))

    for meal_name, products in sorted_meals:
        result += f"{meal_name}:\n"
        if products:
            for name in sorted(products):
                result += f" - {name}\n"

    return result

