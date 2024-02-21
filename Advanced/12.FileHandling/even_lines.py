symbols = {"-", ",", ".", "!", "?"}

with open('files/file_one.txt', 'r') as even_lines_line:
    text = even_lines_line.readlines()

for index in range(0, len(text), 2):
    current_line = text[index]

    for symbol in symbols:
        current_line = current_line.replace(symbol, '@')

    print(current_line[::-1])
