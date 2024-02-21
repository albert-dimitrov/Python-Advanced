from collections import deque

parentheses = deque(input())
open_parentheses = deque()
while parentheses:
    current_parenthesis = parentheses.popleft()
    if current_parenthesis in '({[':
        open_parentheses.append(current_parenthesis)
    elif not open_parentheses:
        print('NO')
        break
    else:
        if f'{open_parentheses.pop() + current_parenthesis}' not in '(){}[]':
            print('NO')
            break
else:
    print("YES")
