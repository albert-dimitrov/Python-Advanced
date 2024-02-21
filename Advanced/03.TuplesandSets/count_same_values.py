numbers = tuple([float(x) for x in input().split()])

same_vals = {}
for num in numbers:
    if num not in same_vals:
        same_vals[num] = numbers.count(num)

for num, count in same_vals.items():
    print(f'{num:.1f} - {count} times')
