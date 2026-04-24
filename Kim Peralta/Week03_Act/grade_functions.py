def calculate_average(grade1_kwap, grade2_kwap, grade3_kwap):
    """Calculate the average of three grades"""
    return (grade1_kwap + grade2_kwap + grade3_kwap) / 3

def get_remark(average_kwap):
    """Return the remark based on the average grade"""
    if average_kwap >= 90:
        return "Excellent"
    elif average_kwap >= 85:
        return "Very Good"
    elif average_kwap >= 80:
        return "Good"
    elif average_kwap >= 75:
        return "Fair"
    else:
        return "Failed"

# Main program
print("----- STUDENT GRADE PROCESSOR -----")
student_name_kwap = input("Enter student name: ")
grade1_kwap = float(input("Enter first grade: "))
grade2_kwap = float(input("Enter second grade: "))
grade3_kwap = float(input("Enter third grade: "))

# Calculate average and get remark
average_kwap = calculate_average(grade1_kwap, grade2_kwap, grade3_kwap)
remark_kwap = get_remark(average_kwap)

# Display results
print("\n----- RESULTS -----")
print("Student Name:", student_name_kwap)
print("Grade 1:", grade1_kwap)
print("Grade 2:", grade2_kwap)
print("Grade 3:", grade3_kwap)
print("Average:", round(average_kwap, 2))
print("Remark:", remark_kwap)
