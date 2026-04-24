class Person_kwap:
    def __init__(self_kwap, name_kwap, age_kwap):
        self_kwap.name_kwap = name_kwap
        self_kwap.age_kwap = age_kwap


class Student_kwap(Person_kwap):
    def __init__(self_kwap, name_kwap, age_kwap, course_kwap):
        super().__init__(name_kwap, age_kwap)
        self_kwap.course_kwap = course_kwap

    def display_student_kwap(self_kwap):
        print("Name:", self_kwap.name_kwap)
        print("Age:", self_kwap.age_kwap)
        print("Course:", self_kwap.course_kwap)


student1_kwap = Student_kwap("Maria", 20, "BSIS")
student1_kwap.display_student_kwap()
