from collections import deque
water = int(input())

names = input()
people = deque()
while names != 'Start':
    people.append(names)

    names = input()

command = input()

while command != 'End':
    data = command.split()
    if len(data) == 1:
        litters_request = int(data[0])
        person = people.popleft()

        if water >= litters_request:
            print(f"{person} got water")
            water -= litters_request
        else:
            print(f"{person} must wait")
    else:
        water += int(data[1])

    command = input()

print(f"{water} liters left")
