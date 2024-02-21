from collections import deque

green_light = int(input())
free_window = int(input())
traffic_line = deque()
passed_cars = 0
crash = False

while True:
    command = input()
    if command == 'END':
        break

    if command != 'green':
        traffic_line.append(command)
    elif command == 'green':
        green = green_light

        while green > 0 and traffic_line:
            car = traffic_line.popleft()
            total_time = green + free_window

            if len(car) > total_time:
                print(f"A crash happened!")
                print(f"{car} was hit at {car[total_time]}.")
                crash = True
                break

            green -= len(car)
            passed_cars += 1

        if crash:
            break

if not crash:
    print("Everyone is safe.")
    print(f"{passed_cars} total cars passed the crossroads.")
