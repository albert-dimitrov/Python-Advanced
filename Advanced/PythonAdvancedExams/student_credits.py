def students_credits(*args):
    diyans_data = {}
    total_credits = 0
    result = ''

    for data in args:
        course_name, credits_to_get, max_points, diyans_points = data.split('-')
        percentage = int(diyans_points) / int(max_points)

        credits_deyan_gets = float(int(credits_to_get) * percentage)
        total_credits += credits_deyan_gets

        diyans_data[course_name] = credits_deyan_gets

    sorted_grades = sorted(diyans_data.items(), key=lambda x: -x[1])

    if total_credits >= 240:
        result += f"Diyan gets a diploma with {total_credits:.1f} credits.\n"
    else:
        result += f"Diyan needs {(240 - total_credits):.1f} credits more for a diploma.\n"

    for name, credit in sorted_grades:
        result += f"{name} - {credit:.1f}\n"

    return result

