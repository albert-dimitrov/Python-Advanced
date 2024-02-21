from collections import deque

elfs_energy = deque([int(x) for x in input().split()])
number_of_materials = [int(x) for x in input().split()]

total_energy_used = 0
total_toys_made = 0

number_tries = 0

while elfs_energy and number_of_materials:
    current_elf = elfs_energy.popleft()

    if current_elf < 5:
        continue

    current_box = number_of_materials.pop()

    number_tries += 1
    current_toys = 0
    bonus_energy = 0

    made_toy = False

    if number_tries % 3 == 0:
        if current_elf >= current_box * 2:

            current_toys += 2
            total_energy_used += current_box * 2
            current_elf -= current_box * 2
            bonus_energy += 1

            made_toy = True
    else:
        if current_elf >= current_box:

            current_toys += 1
            total_energy_used += current_box
            current_elf -= current_box
            bonus_energy += 1

            made_toy = True

    if number_tries % 5 == 0 and made_toy:
        current_toys = 0
        bonus_energy = 0

    if not made_toy:
        current_elf *= 2
        number_of_materials.append(current_box)

    total_toys_made += current_toys
    current_elf += bonus_energy

    elfs_energy.append(current_elf)

print(f"Toys: {total_toys_made}")
print(f"Energy: {total_energy_used}")

if elfs_energy:
    print(f"Elves left: {', '.join([str(x) for x in elfs_energy])}")

if number_of_materials:
    print(f"Boxes left: {', '.join([str(x) for x in number_of_materials])}")
