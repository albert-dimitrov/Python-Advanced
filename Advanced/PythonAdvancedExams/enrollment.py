def gather_credits(credits, *courses):
    enrolled_courses = []
    total_credis = 0
    result = ''

    if credits == 0:
        return f"Enrollment finished! Maximum credits: {total_credis}.\nCourses: {', '.join(sorted(enrolled_courses))}"

    for name, credit in courses:
        if name not in enrolled_courses:
            total_credis += credit
            enrolled_courses.append(name)

        if total_credis >= credits:
            return f"Enrollment finished! Maximum credits: {total_credis}.\nCourses: {', '.join(sorted(enrolled_courses))}"

    return f"You need to enroll in more courses! You have to gather {credits - total_credis} credits more."



print(gather_credits(
    0,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))
