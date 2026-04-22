student_1 = Student("Opeyemi", 200, 82)
student_2 = Student("Olarenwaju", 300, 75)
student_3 = Student("Israel", 100, 50)
student_4 = Student("Olamide", 500, 69)

my_student = [student_1, student_2, student_3, student_4]

if __name__ == "__main__":
    top_students = find_top_three_students(my_student)
    for student in top_students:
        print(student)
        print("-" * 20)
