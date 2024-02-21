input_string = input()

stack = []
text_list = [x for x in input_string]

while text_list:
    last_char = text_list.pop()
    stack.append(last_char)

print("".join(stack))
