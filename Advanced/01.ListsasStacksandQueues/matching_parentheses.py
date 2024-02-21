expression = input()
paren_indexes = []

for index in range(len(expression)):
    if expression[index] == '(':
        paren_indexes.append(index)
    elif expression[index] == ')':
        print(expression[paren_indexes.pop(): index + 1])

