longest_intersection = set()

for _ in range(int(input())):
    first, second = input().split('-')

    start_first, stop_first = [int(x) for x in first.split(',')]
    start_second, stop_second = [int(x) for x in second.split(',')]

    first_set = set(range(start_first, stop_first + 1))
    second_set = set(range(start_second, stop_second + 1))

    intersection = first_set.intersection(second_set)
    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(
    f"Longest intersection is [{', '.join([str(x) for x in longest_intersection])}] with length {len(longest_intersection)}")
