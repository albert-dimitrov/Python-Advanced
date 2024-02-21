numbers_of_guests = int(input())
guests = set()
for _ in range(numbers_of_guests):
    code = input()
    guests.add(code)

while True:
    command = input()

    if command == 'END':
        break

    if command in guests:
        guests.remove(command)

sorted_guests = sorted(guests)
print(len(sorted_guests))
for guest in sorted_guests:
    print(guest)
