number_of_people = int(input())
# people_data = {}
#
# for _ in range(number_of_people):
#     name = input()
#     if name not in people_data:
#         people_data[name] = 1
#     else:
#         people_data[name] += 1
#
# for name in people_data.keys():
#     print(name)
names = []
for _ in range(number_of_people):
    name = input()
    names.append(name)

names = set(names)
for current_name in names:
    print(current_name)