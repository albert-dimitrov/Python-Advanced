def find_pairs(sequence, result):
    for first_number in range(len(sequence)):
        for second_number in range(first_number + 1, len(sequence)):
            if sequence[first_number] + sequence[second_number] == result:
                print(f"{sequence[first_number]} + {sequence[second_number]} = {result}")
                break

numbers = [int(x) for x in input().split()]
target = int(input())
find_pairs(numbers, target)


