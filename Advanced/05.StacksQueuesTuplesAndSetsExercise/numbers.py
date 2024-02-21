def add(sequence, numbers):
    for num in numbers:
        sequence.add(num)

def remove(sequence, numbers):
    for num in numbers:
        sequence.discard(num)

first_sequence = set([int(x) for x in input().split()])
second_sequence = set([int(x) for x in input().split()])

for _ in range(int(input())):
    tokens = input().split()
    operation = tokens[0]

    if operation == 'Add':
        in_a_row = tokens[1]
        numbers = [int(tokens[i]) for i in range(2, len(tokens))]
        if in_a_row == 'First':
            add(first_sequence, numbers)
        elif in_a_row == 'Second':
            add(second_sequence, numbers)
    elif operation == 'Remove':
        in_a_row = tokens[1]
        numbers = [int(tokens[i]) for i in range(2, len(tokens))]
        if in_a_row == 'First':
            remove(first_sequence, numbers)
        elif in_a_row == 'Second':
            remove(second_sequence, numbers)
    elif operation == 'Check':
        print(first_sequence.issubset(second_sequence)\
              or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
