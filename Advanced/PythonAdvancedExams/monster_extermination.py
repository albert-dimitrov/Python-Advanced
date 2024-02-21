from collections import deque

monster_armor = deque([int(x) for x in input().split(',')])
solider_attack = [int(x) for x in input().split(',')]
number_of_monsters_killed = 0

while monster_armor and solider_attack:
    monster = monster_armor.popleft()
    solider = solider_attack.pop()

    if solider >= monster:
        solider -= monster
        number_of_monsters_killed += 1
        if solider > 0:
            if solider_attack:
                solider_attack[-1] += solider
            else:
                solider_attack.append(solider)
    else:
        monster -= solider
        if monster > 0:
            monster_armor.append(monster)


if not monster_armor:
    print("All monsters have been killed!")
if not solider_attack:
    print("The soldier has been defeated.")

print(f"Total monsters killed: {number_of_monsters_killed}")
