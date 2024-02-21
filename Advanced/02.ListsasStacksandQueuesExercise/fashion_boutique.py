box_of_clothes = [int(x) for x in input().split()]
rack_capacity = int(input())
racks_count = 1
current_rack_space = rack_capacity

while box_of_clothes:
    cloth = box_of_clothes.pop()
    if current_rack_space >= cloth:
        current_rack_space -= cloth
    else:
        racks_count += 1
        current_rack_space = rack_capacity - cloth

print(racks_count)
