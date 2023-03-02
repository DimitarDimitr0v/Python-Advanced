def students_credits(*data):

    course_information = {}
    course_credit_calculated = {}
    total_student_credits = 0
    final_strings = []

    for el in data:
        current_data = el.split("-")
        course_information[current_data[0]] = [int(x) for x in current_data[1::]]

    for course, grade in course_information.items():
        course_credits = grade[0]
        total_points = grade[1]
        student_points = grade[2]

        percentage = student_points / total_points
        student_credits = course_credits * percentage

        course_credit_calculated[course] = student_credits
        total_student_credits += student_credits

    sorted_course_and_credits_info = dict(sorted(course_credit_calculated.items(), key=lambda x: -x[1]))

    if total_student_credits >= 240:
        final_strings.append(f"Diyan gets a diploma with {total_student_credits:.1f} credits.")
    else:
        final_strings.append(f"Diyan needs {240 - total_student_credits:.1f} credits more for a diploma.")

    for course, points in sorted_course_and_credits_info.items():
        final_strings.append(f"{course} - {float(points):.1f}")

    return "\n".join(final_strings)


print(
    students_credits(
        "Discrete Maths-40-500-450",
        "AI Development-20-400-400",
        "Algorithms Advanced-50-700-630",
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Game Engine Development-70-100-70",
        "Mobile Development-25-250-225",
        "QA-20-300-300",
    )
)
