# Original grades dictionary
student_grades = {
    "Alice": [85, 90, 78, 92],
    "Bob": [76, 88, 95],
    "Charlie": [82, 89, 75, 81, 90],
    "David": [92, 95, 88]
}

# Calculate average grades
average_grades = {}

for student, grades in student_grades.items():
    # Calculate average for current student
    total = 0
    for grade in grades:
        total += grade
    average = total / len(grades)
    
    # Add to new dictionary
    average_grades[student] = round(average, 2)

# Print results
print("Original grades dictionary:")
for student, grades in student_grades.items():
    print(f"{student}: {grades}")

print("\nAverage grades dictionary:")
for student, average in average_grades.items():
    print(f"{student}: {average}")