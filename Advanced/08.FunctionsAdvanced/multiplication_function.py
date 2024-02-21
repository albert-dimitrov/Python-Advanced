def multiply(*args):
    total_sum = args[0]

    for num in args[1:]:
        total_sum *= num

    return total_sum
