print("----- GRADE LIST ANALYZER -----")
grades_kwap = []

# Ask user to enter 5 grades
for i_kwap in range(1, 6):
    grade_kwap = float(input(f"Enter grade {i_kwap}: "))
    grades_kwap.append(grade_kwap)

# Compute statistics
average_grade_kwap = sum(grades_kwap) / len(grades_kwap)
highest_grade_kwap = max(grades_kwap)
lowest_grade_kwap = min(grades_kwap)

# Display results
print("\n----- RESULTS -----")
print("Grades:", grades_kwap)
print("Average Grade:", round(average_grade_kwap, 1))
print("Highest Grade:", highest_grade_kwap)
print("Lowest Grade:", lowest_grade_kwap)
