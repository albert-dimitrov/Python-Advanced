even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    name = input()
    value_of_name = 0

    for char in name:
        value_of_name += ord(char)

    total_value = value_of_name // row

    if total_value % 2 == 0:
        even_set.add(total_value)
    else:
        odd_set.add(total_value)

if sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=', ')
elif sum(odd_set) > sum(even_set):
    print(*odd_set.difference(even_set), sep=', ')
elif sum(even_set) > sum(odd_set):
    print(*odd_set.symmetric_difference(even_set), sep=', ')
