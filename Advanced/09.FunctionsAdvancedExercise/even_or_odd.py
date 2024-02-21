def even_odd(*args):
    command = args[-1]

    if command == 'even':
        return [int(x) for x in args[:len(args) - 1] if int(x) % 2 == 0]
    elif command == 'odd':
        return [int(x) for x in args[:len(args) - 1] if int(x) % 2 != 0]
