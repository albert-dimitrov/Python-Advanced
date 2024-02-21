def operation(rows, stack):
    for row in range(rows):
        command = input().split()

        if command[0] == '1':
            stack.append(int(command[1]))
        elif command[0] == '2':
            if stack:
                stack.pop()
        elif command[0] == '3':
            if stack:
                print(max(stack))
        elif command[0] == '4':
            if stack:
                print(min(stack))
    return stack

def main():
    numbers_of_rows = int(input())
    numbers = []

    stack = operation(numbers_of_rows, numbers)
    stack.reverse()

    print(*stack, sep=', ')

main()
