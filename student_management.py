# Student Information Management System

students = []
DATA_FILE = "students.txt"

print("Student Information Management System")
print("System initialized successfully!")


# --------------------------------------------------
# 1. Grade Calculation
# --------------------------------------------------

def calculate_grade(marks):

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    elif marks >= 40:
        return "E"
    else:
        return "F"


# --------------------------------------------------
# 2. Add Student
# --------------------------------------------------

def add_student():

    print("\n--- Add Student ---")

    student_id = input("Enter Student ID: ").strip()

    # Check duplicate ID
    for student in students:
        if student["id"] == student_id:
            print("Student ID already exists.")
            return

    name = input("Enter Name: ").strip()
    age = input("Enter Age: ").strip()
    gender = input("Enter Gender: ").strip()
    course = input("Enter Course: ").strip()
    semester = input("Enter Semester: ").strip()
    email = input("Enter Email: ").strip()
    phone = input("Enter Phone: ").strip()

    # Validate marks
    while True:

        try:
            marks = float(input("Enter Marks (0-100): "))

            if 0 <= marks <= 100:
                break

            print("Marks must be between 0 and 100.")

        except ValueError:
            print("Please enter a valid number.")

    # Create student dictionary
    student = {
        "id": student_id,
        "name": name,
        "age": age,
        "gender": gender,
        "course": course,
        "semester": semester,
        "email": email,
        "phone": phone,
        "marks": marks,
        "grade": calculate_grade(marks)
    }

    students.append(student)

    print("Student added successfully!")


# --------------------------------------------------
# 3. Display All Students
# --------------------------------------------------

def display_students():

    print("\n--- All Students ---")

    if not students:
        print("No student records found.")
        return

    for student in students:

        print("-" * 45)

        print("Student ID :", student["id"])
        print("Name       :", student["name"])
        print("Age        :", student["age"])
        print("Gender     :", student["gender"])
        print("Course     :", student["course"])
        print("Semester   :", student["semester"])
        print("Email      :", student["email"])
        print("Phone      :", student["phone"])
        print("Marks      :", student["marks"])
        print("Grade      :", student["grade"])

        print("-" * 45)


# --------------------------------------------------
# 4. Search Student
# --------------------------------------------------

def search_student():

    print("\n--- Search Student ---")

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("\nStudent Found!")
            print("-" * 45)

            for key, value in student.items():
                print(f"{key.capitalize():10}: {value}")

            return

    print("Student not found.")


# --------------------------------------------------
# 5. Update Student
# --------------------------------------------------

def update_student():

    print("\n--- Update Student ---")

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            print("Leave a field blank to keep its current value.")

            name = input(
                f"Name [{student['name']}]: "
            ).strip()

            course = input(
                f"Course [{student['course']}]: "
            ).strip()

            semester = input(
                f"Semester [{student['semester']}]: "
            ).strip()

            email = input(
                f"Email [{student['email']}]: "
            ).strip()

            phone = input(
                f"Phone [{student['phone']}]: "
            ).strip()

            if name:
                student["name"] = name

            if course:
                student["course"] = course

            if semester:
                student["semester"] = semester

            if email:
                student["email"] = email

            if phone:
                student["phone"] = phone

            marks_input = input(
                f"Marks [{student['marks']}]: "
            ).strip()

            if marks_input:

                try:

                    marks = float(marks_input)

                    if 0 <= marks <= 100:

                        student["marks"] = marks
                        student["grade"] = calculate_grade(marks)

                    else:

                        print(
                            "Invalid marks. Previous marks retained."
                        )

                except ValueError:

                    print(
                        "Invalid marks. Previous marks retained."
                    )

            print(
                "Student information updated successfully!"
            )

            return

    print("Student not found.")


# --------------------------------------------------
# 6. Delete Student
# --------------------------------------------------

def delete_student():

    print("\n--- Delete Student ---")

    student_id = input("Enter Student ID: ").strip()

    for student in students:

        if student["id"] == student_id:

            students.remove(student)

            print("Student deleted successfully!")

            return

    print("Student not found.")


# --------------------------------------------------
# 7. Save Data to File
# --------------------------------------------------

def save_data():

    try:

        with open(DATA_FILE, "w") as file:

            for student in students:

                line = "|".join([
                    student["id"],
                    student["name"],
                    student["age"],
                    student["gender"],
                    student["course"],
                    student["semester"],
                    student["email"],
                    student["phone"],
                    str(student["marks"]),
                    student["grade"]
                ])

                file.write(line + "\n")

        print("Student data saved successfully.")

    except Exception as e:

        print("Error while saving data:", e)


# --------------------------------------------------
# 8. Load Data from File
# --------------------------------------------------

def load_data():

    students.clear()

    try:

        with open(DATA_FILE, "r") as file:

            for line in file:

                data = line.strip().split("|")

                if len(data) == 10:

                    student = {
                        "id": data[0],
                        "name": data[1],
                        "age": data[2],
                        "gender": data[3],
                        "course": data[4],
                        "semester": data[5],
                        "email": data[6],
                        "phone": data[7],
                        "marks": float(data[8]),
                        "grade": data[9]
                    }

                    students.append(student)

        print(f"{len(students)} student record(s) loaded.")

    except FileNotFoundError:

        print(
            "No previous data file found. "
            "Starting with empty records."
        )

    except Exception as e:

        print("Error while loading data:", e)


# --------------------------------------------------
# 9. Main Menu
# --------------------------------------------------

def main_menu():

    while True:

        print("\n" + "=" * 50)
        print("     STUDENT INFORMATION MANAGEMENT SYSTEM")
        print("=" * 50)

        print("1. Add Student")
        print("2. Display All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Save Data")
        print("7. Load Data")
        print("8. Exit")

        print("=" * 50)

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":

            add_student()

        elif choice == "2":

            display_students()

        elif choice == "3":

            search_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "6":

            save_data()

        elif choice == "7":

            load_data()

        elif choice == "8":

            save_data()

            print(
                "Thank you for using the Student "
                "Information Management System!"
            )

            break

        else:

            print(
                "Invalid choice. Please select a number from 1 to 8."
            )


# --------------------------------------------------
# START APPLICATION
# --------------------------------------------------

load_data()
main_menu()