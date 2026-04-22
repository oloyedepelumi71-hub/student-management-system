def find_best_student(students):
    best_student = students[0]
    for student in students:
        if student.score > best_student.score:
            best_student = student
    return best_student

def find_top_three_students(students):
    sorted_students = sorted(
        students, key=lambda student: student.score, reverse=True)
    return sorted_students[: 3]
