class Student_kwap:
    def __init__(self_kwap, name_kwap, student_id_kwap, course_kwap):
        self_kwap.name_kwap = name_kwap
        self_kwap.student_id_kwap = student_id_kwap
        self_kwap.course_kwap = course_kwap
    
    def display_student_kwap(self_kwap):
        print("Name:", self_kwap.name_kwap)
        print("Student ID:", self_kwap.student_id_kwap)
        print("Course:", self_kwap.course_kwap)

student1_kwap = Student_kwap("Maria", "2023-001", "BSIS")
student1_kwap.display_student_kwap()
