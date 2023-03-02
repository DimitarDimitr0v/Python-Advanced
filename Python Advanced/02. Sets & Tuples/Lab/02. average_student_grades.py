def data_arrangement(f_students):
    total_students = []
    for _ in range(f_students):
        total_students.append(input())

    return total_students


def average_calculation(f_grades):
    return sum(f_grades) / len(f_grades)


n = int(input())
students_info = data_arrangement(n)

student_grades = {}

for el in students_info:
    name, grade = el.split(' ')

    if name not in student_grades:
        student_grades[name] = []
    student_grades[name].append(float(grade))

for (students, grades) in student_grades.items():
    data = ' '.join(map(lambda grades_formation: f"{grades_formation:.2f}", [x for x in grades]))
    print(f"{students} -> {data} (avg: {average_calculation(grades):.2f})")
