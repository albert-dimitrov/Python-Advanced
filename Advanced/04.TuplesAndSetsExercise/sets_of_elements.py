first, second = [int(x) for x in input().split()]
first_set = set()
second_set = set()
for _ in range(first):
    number = int(input())
    first_set.add(number)

for _ in range(second):
    number = int(input())
    second_set.add(number)

print(*first_set.intersection(second_set), sep="\n")
