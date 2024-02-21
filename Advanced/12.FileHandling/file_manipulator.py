import os

while True:
    command, *tokens = input().split('-')

    if command == 'End':
        break

    if command == 'Create':
        with open(f"C:\\Users\\EMI\\PycharmProjects\\PB-Exam\\files\\{tokens[0]}", 'w'):
            pass

    elif command == 'Add':
        with open(f"C:\\Users\\EMI\\PycharmProjects\\PB-Exam\\files\\{tokens[0]}", 'a') as file:
            file.write(f"{tokens[1]}\n")

    elif command == 'Replace':
        try:
            with open(f"C:\\Users\\EMI\\PycharmProjects\\PB-Exam\\files\\{tokens[0]}", 'r+') as file:
                text = file.read()
                text = text.replace(tokens[1], tokens[2])

                file.seek(0)
                file.write(text)
                file.truncate()

        except FileNotFoundError:
            print('Error occurred')

    elif command == 'Delet':
        try:
            os.remove(f"C:\\Users\\EMI\\PycharmProjects\\PB-Exam\\files\\{tokens[0]}")

        except FileNotFoundError:
            print('Error occurred')

