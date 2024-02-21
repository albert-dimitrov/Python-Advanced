from collections import deque

materials = [int(x) for x in input().split()]
magic = deque([int(x) for x in input().split()])
toys = []
presents = {
    150: 'Doll',
    250: 'Wooden train',
    300: 'Teddy bear',
    400: 'Bicycle',
}

while materials and magic:
    material = materials.pop() if magic[0] or not materials[-1] else 0
    curr_magic = magic.popleft() if material or not magic[0] else 0

    if not curr_magic:
        continue

    product = material * curr_magic

    if presents.get(product):
        toys.append(presents[product])
    elif product < 0:
        materials.append(material + curr_magic)
    elif product > 0:
        materials.append(material + 15)

if {'Doll', 'Wooden train'}.issubset(toys) or {'Teddy bear', 'Bicycle'}.issubset(toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")

if materials:
    print(f"Materials left: {', '.join(str(x) for x in materials[::-1])}")
if magic:
    print(f"Magic left: {', '.join(str(x) for x in magic)}")

print(*[f"{toy}: {toys.count(toy)}" for toy in sorted(set(toys))], sep="\n")

