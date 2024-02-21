matrix = [[x for x in row.split()] for row in input().split('|')]
[print(*row, end=' ') for row in matrix[::-1] if row]


# matrix = [[x for x in row.split()] for row in input().split('|')]
# for row in matrix[::-1]:
#     print(*row, end=' ')



# line = input().split('|')
# sub_list = []
#
# for sub_str in line[::-1]:
#     sub_list.extend(sub_str.split())
# print(*sub_list)
