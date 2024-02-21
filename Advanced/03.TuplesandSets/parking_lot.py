numbers_of_lines = int(input())
parking_lot = set()
for _ in range(numbers_of_lines):
    operation, plate = input().split(', ')
    if operation == 'IN':
        parking_lot.add(plate)
    elif operation == "OUT":
        parking_lot.remove(plate)

if not parking_lot:
    print("Parking Lot is Empty")
else:
    for plate in parking_lot:
        print(plate)
