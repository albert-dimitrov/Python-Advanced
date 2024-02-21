number_of_students = int(input())
students_data = {}
for _ in range(number_of_students):
    name, grade = input().split()
    grade = float(grade)
    if name not in students_data:
        students_data[name] = [grade]
    else:
        students_data[name].append(grade)

for student, data in students_data.items():
    average_grade = sum(data) / len(data)
    formatted_grades = f'{" ".join([f"{x:.2f}" for x in data])}'
    print(f"{student} -> {formatted_grades} (avg: {average_grade:.2f})")
