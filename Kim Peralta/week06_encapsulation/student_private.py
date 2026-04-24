class Student_kwap:
    def __init__(self_kwap, name_kwap, student_id_kwap, gpa_kwap):
        self_kwap.__name = name_kwap
        self_kwap.__student_id = student_id_kwap
        self_kwap.__gpa = gpa_kwap

    def get_student_info_kwap(self_kwap):
        print("Name:", self_kwap.__name)
        print("Student ID:", self_kwap.__student_id)
        print("GPA:", self_kwap.__gpa)


student1_kwap = Student_kwap("Juan", "2023-001", 1.75)
student1_kwap.get_student_info_kwap()
