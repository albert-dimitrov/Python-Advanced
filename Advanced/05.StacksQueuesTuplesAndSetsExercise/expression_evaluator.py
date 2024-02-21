from collections import deque
from math import floor

expression = deque(input().split())
operators = ["*", "+", "-", "/"]
current_numbers = deque()

while expression:
    symbol = expression.popleft()

    if symbol not in operators:
        current_numbers.append(int(symbol))
    else:
        if symbol == "*":
            num = current_numbers.popleft()
            while current_numbers:
                num *= current_numbers.popleft()
            current_numbers.append(num)
        elif symbol == "+":
            num = current_numbers.popleft()
            while current_numbers:
                num += current_numbers.popleft()
            current_numbers.append(num)
        elif symbol == "-":
            num = current_numbers.popleft()
            while current_numbers:
                num -= current_numbers.popleft()
            current_numbers.append(num)
        elif symbol == "/":
            num = current_numbers.popleft()
            while current_numbers:
                num /= current_numbers.popleft()
            current_numbers.append(floor(num))

print(*current_numbers)
