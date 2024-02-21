number_of_lines = int(input())
unique_elements = set()

for _ in range(number_of_lines):
    current_elements = input().split()
    for element in current_elements:
        unique_elements.add(element)

print("\n".join([x for x in unique_elements]))
