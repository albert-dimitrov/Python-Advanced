def age_assignment(*args, **kwargs):
    people_data = {}
    text = ''

    for name in args:
        letter = name[:1]
        people_data[name] = kwargs[letter]

    sorted_data = sorted(people_data.items(), key=lambda x: x[0])

    for name, age in sorted_data:
        text += f"{name} is {age} years old.\n"

    return text
