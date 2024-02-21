def math_operations(*numbers, **operations):
    num_count = 0

    for num in numbers:
        num_count += 1
        if num_count == 1:
            operations['a'] += num
        elif num_count == 2:
            operations['s'] -= num
        elif num_count == 3:
            if num == 0 or operations['d'] == 0:
                continue
            operations['d'] /= num
        elif num_count == 4:
            num_count = 0
            operations['m'] *= num

    sorted_operations = sorted(operations.items(), key=lambda x: (-x[1], x[0]))

    return '\n'.join([f"{key}: {value:.1f}" for key, value in sorted_operations])
