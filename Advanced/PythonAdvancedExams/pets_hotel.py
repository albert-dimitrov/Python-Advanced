def accommodate_new_pets(capacity, max_weight, *args):
    hotel = {}
    print_text = ''
    for pet, weight in args:
        if capacity == 0:
            print_text += f"You did not manage to accommodate all pets!\n"
            break

        if weight <= max_weight:
            if pet not in hotel:
                hotel[pet] = 0

            hotel[pet] += 1
            capacity -= 1
    else:
        print_text += f"All pets are accommodated! Available capacity: {capacity}.\n"

    sorted_hotel = sorted(hotel.items(), key=lambda x: x[0])

    print_text += "Accommodated pets:\n" + '\n'.join([f'{pet_type}: {number}' for pet_type, number in sorted_hotel])
    return print_text

print(accommodate_new_pets(
    10,
    10.0,
    ("cat", 5.8),
    ("dog", 10.5),
    ("parrot", 0.8),
    ("cat", 3.1),
))
