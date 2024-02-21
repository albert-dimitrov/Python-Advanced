def cookbook(*food_data):
    cuisine_data = {}
    return_result = ''

    for recipe_name, cuisine, ingredients in food_data:
        if cuisine not in cuisine_data:
            cuisine_data[cuisine] = {}

        cuisine_data[cuisine][recipe_name] = ingredients

    sorted_cuisine = sorted(cuisine_data.items(), key=lambda x: (-len(x[1]), x[0]))

    for cuisine_name, recipes in sorted_cuisine:
        return_result += f"{cuisine_name} cuisine contains {len(recipes)} recipes:\n"
        for name, curr_ingredients in sorted(recipes.items(), key=lambda x: x[0]):
            return_result += f'  * {name} -> Ingredients: {", ".join(curr_ingredients)}\n'

    return return_result


