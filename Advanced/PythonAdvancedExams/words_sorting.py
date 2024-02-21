def words_sorting(*args):
    words_data = {}
    total_sum = 0

    result = ''

    for word in args:
        word_sum = 0

        for char in word:
            word_sum += ord(char)

        total_sum += word_sum
        words_data[word] = word_sum

    if total_sum % 2 != 0:
        sorted_data = sorted(words_data.items(), key=lambda x: -x[1])
    else:
        sorted_data = sorted(words_data.items(), key=lambda x: x[0])

    for key, value in sorted_data:
        result += f"{key} - {value}\n"

    return result

