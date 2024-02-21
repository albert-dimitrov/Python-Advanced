def sorting_cheeses(**kwargs):
    result = ''

    sorted_kwarg = sorted(
        kwargs.items(),
        key=lambda x: (-len(x[1]), x[0])
    )

    for name, quantity in sorted_kwarg:
        result += name + '\n'
        for num in sorted(quantity, reverse=True):
            result += f'{num}\n'

    return result
