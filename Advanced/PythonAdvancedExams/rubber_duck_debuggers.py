from collections import deque

def decrease_task(time, current_tasks):
    current_tasks -= 2
    if not (current_tasks <= 0):
        number_of_tasks.append(current_tasks)

    time_to_complete_task.append(time)


def check_type(total_time):
    if 0 <= total_time <= 60:
        return 'Darth Vader Ducky'
    elif 61 <= total_time <= 120:
        return 'Thor Ducky'
    elif 121 <= total_time <= 180:
        return 'Big Blue Rubber Ducky'
    elif 181 <= total_time <= 240:
        return 'Small Yellow Rubber Ducky'
    else:
        decrease_task(time, current_tasks)
        return None

def add_type(duck_type):
    if duck_type not in duck_types.keys():
        duck_types[duck_type] = 0

    duck_types[duck_type] += 1

def printing(duck_types):

    print(f"Darth Vader Ducky: {duck_types['Darth Vader Ducky']}")
    print(f"Thor Ducky: {duck_types['Thor Ducky']}")
    print(f"Big Blue Rubber Ducky: {duck_types['Big Blue Rubber Ducky']}")
    print(f"Small Yellow Rubber Ducky: {duck_types['Small Yellow Rubber Ducky']}")


time_to_complete_task = deque([int(x) for x in input().split()])
number_of_tasks = [int(x) for x in input().split()]

duck_types = {
    'Darth Vader Ducky': 0,
    'Thor Ducky': 0,
    'Big Blue Rubber Ducky': 0,
    'Small Yellow Rubber Ducky': 0
}

while time_to_complete_task and number_of_tasks:
    time = time_to_complete_task.popleft()
    current_tasks = number_of_tasks.pop()

    total_time = time * current_tasks

    duck_type = check_type(total_time)

    if duck_type:
        add_type(duck_type)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")

printing(duck_types)

