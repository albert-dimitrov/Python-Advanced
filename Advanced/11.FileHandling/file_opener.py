import os.path
import re

words_path = os.path.join('words.txt')
input_path = os.path.join('my_first_file.txt')
words_count = {}

with open(words_path) as file:
    searched_words = file.read().split()
    searched_word = [x.lower() for x in searched_words]

with open(input_path) as file:
    content = file.read().lower()


for word in searched_word:
    regex = re.compile(rf"\b{word}\b")
    count = re.findall(regex, content)
    words_count[word] = len(count)

sorted_word_count = sorted(words_count.items(), key=lambda x: -x[1])
for k, v in sorted_word_count:
    print(f'{k} - {v}')