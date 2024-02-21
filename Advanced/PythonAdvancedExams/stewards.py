from collections import deque

seats = input().split(', ')

first_sequence = deque([int(x) for x in input().split(', ')])
second_sequence = deque([int(x) for x in input().split(', ')])

seated_seats = []

total_rotations = 0

while first_sequence and second_sequence:
    if total_rotations == 10 or len(seated_seats) == 3:
        break

    first_number = first_sequence.popleft()
    second_number = second_sequence.pop()

    their_ascii = chr(first_number + second_number)

    seat_variant_one = f'{first_number}{their_ascii}'
    seat_variant_two = f'{second_number}{their_ascii}'
    total_rotations += 1

    if seat_variant_one in seated_seats or seat_variant_two in seated_seats:
        continue

    if seat_variant_one in seats:
        seated_seats.append(seat_variant_one)
        found = True
    elif seat_variant_two in seats:
        seated_seats.append(seat_variant_two)
        found = True
    else:
        first_sequence.append(first_number)
        second_sequence.appendleft(second_number)

print(f"Seat matches: {', '.join(seated_seats)}")
print(f"Rotations count: {total_rotations}")
