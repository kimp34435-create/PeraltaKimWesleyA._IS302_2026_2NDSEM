class Person_kwap:
    def __init__(self_kwap, name_kwap, age_kwap):
        self_kwap.name_kwap = name_kwap
        self_kwap.age_kwap = age_kwap

    def display_info_kwap(self_kwap):
        print("Name:", self_kwap.name_kwap)
        print("Age:", self_kwap.age_kwap)


class Student_kwap(Person_kwap):
    def __init__(self_kwap, name_kwap, age_kwap, course_kwap):
        super().__init__(name_kwap, age_kwap)
        self_kwap.course_kwap = course_kwap

    def display_info_kwap(self_kwap):
        super().display_info_kwap()
        print("Course:", self_kwap.course_kwap)


class Teacher_kwap(Person_kwap):
    def __init__(self_kwap, name_kwap, age_kwap, subject_kwap):
        super().__init__(name_kwap, age_kwap)
        self_kwap.subject_kwap = subject_kwap

    def display_info_kwap(self_kwap):
        super().display_info_kwap()
        print("Subject:", self_kwap.subject_kwap)


# Example usage
student_kwap = Student_kwap("Maria", 20, "BSIS")
teacher_kwap = Teacher_kwap("Mr. Smith", 45, "Mathematics")

print("Student Info:")
student_kwap.display_info_kwap()

print("\nTeacher Info:")
teacher_kwap.display_info_kwap()
