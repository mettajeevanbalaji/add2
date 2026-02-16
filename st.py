# ==============================
# Student Performance Tracker
# ==============================

students = {}      # {student_id: {"name": "", "grade": "", "courses": {}}}
courses = {}       # {course_id: {"name": "", "instructor": ""}}


# ------------------------------
# 1. Add Student
# ------------------------------
def add_student(student_id, name, grade):
    if student_id in students:
        print("Student ID already exists!")
        return
    students[student_id] = {
        "name": name,
        "grade": grade,
        "courses": {}
    }
    print("Student added successfully!")


# ------------------------------
# 2. Add Course
# ------------------------------
def add_course(course_id, course_name, instructor):
    if course_id in courses:
        print("Course ID already exists!")
        return
    courses[course_id] = {
        "name": course_name,
        "instructor": instructor
    }
    print("Course added successfully!")


# ------------------------------
# 3. Record Marks
# ------------------------------
def record_marks(student_id, course_id, marks):
    if student_id not in students:
        print("Invalid student ID!")
        return
    if course_id not in courses:
        print("Invalid course ID!")
        return

    students[student_id]["courses"].setdefault(course_id, {
        "marks": None,
        "attendance": {"present": 0, "total": 0}
    })

    students[student_id]["courses"][course_id]["marks"] = marks
    print("Marks recorded successfully!")


# ------------------------------
# 4. Record Attendance
# ------------------------------
def record_attendance(student_id, course_id, present):
    if student_id not in students:
        print("Invalid student ID!")
        return
    if course_id not in courses:
        print("Invalid course ID!")
        return

    students[student_id]["courses"].setdefault(course_id, {
        "marks": None,
        "attendance": {"present": 0, "total": 0}
    })

    students[student_id]["courses"][course_id]["attendance"]["total"] += 1
    if present:
        students[student_id]["courses"][course_id]["attendance"]["present"] += 1

    print("Attendance recorded successfully!")


# ------------------------------
# 5. Calculate GPA
# ------------------------------
def calculate_gpa(student_id):
    if student_id not in students:
        print("Invalid student ID!")
        return 0

    total_marks = 0
    count = 0

    for course in students[student_id]["courses"].values():
        if course["marks"] is not None:
            total_marks += course["marks"]
            count += 1

    if count == 0:
        return 0

    avg = total_marks / count
    gpa = (avg / 100) * 10
    return round(gpa, 2)


# ------------------------------
# 6. Generate Report Card
# ------------------------------
def generate_report_card(student_id):
    if student_id not in students:
        print("Invalid student ID!")
        return

    student = students[student_id]
    gpa = calculate_gpa(student_id)

    total_present = 0
    total_classes = 0
    top_subjects = []

    for cid, data in student["courses"].items():
        if data["marks"] is not None:
            top_subjects.append((courses[cid]["name"], data["marks"]))

        total_present += data["attendance"]["present"]
        total_classes += data["attendance"]["total"]

    attendance_percent = 0
    if total_classes > 0:
        attendance_percent = round((total_present / total_classes) * 100, 2)

    top_subjects.sort(key=lambda x: x[1], reverse=True)
    top_display = ", ".join([f"{sub} ({mark})" for sub, mark in top_subjects[:2]])

    print("\n=== REPORT CARD ===")
    print(f"Student: {student['name']} ({student_id})")
    print(f"Grade: {student['grade']}")
    print(f"GPA: {gpa}")
    print(f"Attendance: {attendance_percent}%")
    print(f"Top Subjects: {top_display if top_display else 'N/A'}")

    if gpa >= 8:
        print("Remarks: Excellent progress!")
    elif gpa >= 6:
        print("Remarks: Good performance.")
    else:
        print("Remarks: Needs improvement.")


# ------------------------------
# 7. View Top Performers
# ------------------------------
def get_top_performers(grade, count):
    grade_students = [
        (sid, calculate_gpa(sid))
        for sid, s in students.items()
        if s["grade"] == grade
    ]

    grade_students.sort(key=lambda x: x[1], reverse=True)

    print("\nTop Performers:")
    for sid, gpa in grade_students[:count]:
        print(f"{students[sid]['name']} ({sid}) - GPA: {gpa}")


# ------------------------------
# 8. Course-Wise Average
# ------------------------------
def course_average(course_id):
    if course_id not in courses:
        print("Invalid course ID!")
        return

    total = 0
    count = 0

    for student in students.values():
        if course_id in student["courses"]:
            marks = student["courses"][course_id]["marks"]
            if marks is not None:
                total += marks
                count += 1

    if count == 0:
        print("No marks recorded for this course.")
        return

    print("Course Average:", round(total / count, 2))


# ------------------------------
# 9. Attendance Summary
# ------------------------------
def attendance_summary(student_id):
    if student_id not in students:
        print("Invalid student ID!")
        return

    print("\nAttendance Summary:")
    for cid, data in students[student_id]["courses"].items():
        total = data["attendance"]["total"]
        present = data["attendance"]["present"]
        percent = (present / total * 100) if total > 0 else 0
        print(f"{courses[cid]['name']}: {round(percent,2)}%")


# ------------------------------
# Main Menu
# ------------------------------
def main():
    while True:
        print("\nStudent Performance Tracker")
        print("1. Add New Student")
        print("2. Add New Course")
        print("3. Record Marks")
        print("4. Record Attendance")
        print("5. Calculate GPA")
        print("6. Generate Report Card")
        print("7. View Top Performers")
        print("8. View Course-Wise Averages")
        print("9. View Attendance Summary")
        print("10. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            sid = input("Student ID: ")
            name = input("Name: ")
            grade = input("Grade: ")
            add_student(sid, name, grade)

        elif choice == "2":
            cid = input("Course ID: ")
            cname = input("Course Name: ")
            inst = input("Instructor: ")
            add_course(cid, cname, inst)

        elif choice == "3":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            marks = float(input("Marks (0-100): "))
            record_marks(sid, cid, marks)

        elif choice == "4":
            sid = input("Student ID: ")
            cid = input("Course ID: ")
            present = input("Present? (y/n): ").lower() == "y"
            record_attendance(sid, cid, present)

        elif choice == "5":
            sid = input("Student ID: ")
            print("GPA:", calculate_gpa(sid))

        elif choice == "6":
            sid = input("Student ID: ")
            generate_report_card(sid)

        elif choice == "7":
            grade = input("Grade: ")
            count = int(input("How many top students? "))
            get_top_performers(grade, count)

        elif choice == "8":
            cid = input("Course ID: ")
            course_average(cid)

        elif choice == "9":
            sid = input("Student ID: ")
            attendance_summary(sid)

        elif choice == "10":
            print("Exiting...")
            break

        else:
            print("Invalid choice! Try again.")


main()
