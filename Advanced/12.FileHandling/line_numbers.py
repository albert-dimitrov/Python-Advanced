from string import punctuation

with open('files/file_one.txt', 'r') as text_file:
    text = text_file.readlines()

output_file = open('files/output.txt', 'w')

for i in range(len(text)):
    letters, marks = 0, 0

    for symbol in text[i]:

        if symbol.isalpha():
            letters += 1
        elif symbol in punctuation:
            marks += 1

    output_file.write(f"Line {i + 1}: {text[i][:-1]} ({letters})({marks})\n")

output_file.close()
