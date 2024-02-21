def softuni_students(*args, **kwargs):
    user_data = {}
    invalid_students = []
    return_text = ''

    for id, username in args:
        try:
            if username not in user_data:
                user_data[username] = kwargs[id]
        except KeyError:
            invalid_students.append(username)
            continue

    sorted_user_data = sorted(user_data.items(), key=lambda x: x[0])

    for name, course in sorted_user_data:
        return_text += f"*** A student with the username {name} has successfully finished the course {course}!\n"

    if invalid_students:
        invalid_students = sorted(invalid_students)
        return_text += f"!!! Invalid course students: {', '.join(invalid_students)}"

    return return_text
