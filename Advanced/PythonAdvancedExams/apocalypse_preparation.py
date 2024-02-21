from collections import deque


def operation():
    global medicament

    for item, value in items_info.items():
        if combine_number == value:
            if item not in created_items:
                created_items[item] = 0

            created_items[item] += 1
            return
    else:
        if combine_number > 100:
            if 'MedKit' not in created_items:
                created_items['MedKit'] = 0

            created_items['MedKit'] += 1
            left = combine_number - 100

            if medicaments:
                medicaments[-1] += left
        else:
            medicament += 10
            medicaments.append(medicament)


def printing(textiles, medicaments, items):
    if not textiles and not medicaments:
        print("Textiles and medicaments are both empty.")
    elif not textiles:
        print("Textiles are empty.")
    elif not medicaments:
        print("Medicaments are empty.")

    for key, value in items:
        print(f"{key} - {value}")

    if medicaments:
        print(f"Medicaments left: {', '.join([str(x) for x in medicaments[::-1]])}")

    if textiles:
        print(f"Textiles left: {', '.join([str(x) for x in textiles])}")

textiles = deque([int(x) for x in input().split()])
medicaments = [int(x) for x in input().split()]

items_info = {
    'Patch': 30,
    'Bandage': 40,
    'MedKit': 100,
}

created_items = {}

while textiles and medicaments:
    textile = textiles.popleft()
    medicament = medicaments.pop()

    combine_number = textile + medicament

    operation()


sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))
printing(textiles, medicaments, sorted_items)
