name_kwap = input("Enter student name: ")
course_kwap = input("Enter course: ")

with open("students.txt", "a") as file_kwap:
    file_kwap.write(name_kwap + "," + course_kwap + "\n")

print("\nStudent Records")

with open("students.txt", "r") as file_kwap:
    for line_kwap in file_kwap:
        print(line_kwap.strip())
