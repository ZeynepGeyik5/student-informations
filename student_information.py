def add_student(students, name, student_id):
    if student_id in students:
        print(f"Error: Student with ID {student_id} already exists.")
    else:
        students[student_id] = {"name": name, "courses": {}, "average": 0.0}
        print(f"Student {name} with ID {student_id} added successfully!")

def add_course_and_score(students, student_id, course, score):
    if student_id in students:
        students[student_id]["courses"][course] = score
        update_average(students, student_id)
    else:
        print("Student not found.")

def update_average(students, student_id):
    courses = students[student_id]["courses"]
    if courses:
        total_score = sum(courses.values())
        average = total_score / len(courses)
        students[student_id]["average"] = average

def display_student_info(students, student_id):
    if student_id in students:
        student = students[student_id]
        print(f"Student Name: {student['name']}")
        print(f"Courses and Scores: {student['courses']}")
        print(f"Average Score: {student['average']:.2f}")
    else:
        print("Student not found.")

def main():
    students = {}  
    while True:
        print("\n1. Add Student")
        print("2. Add Course and Score")
        print("3. View Student Info")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter student name: ")
            student_id = input("Enter student ID: ")
            add_student(students, name, student_id)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            course = input("Enter course name: ")
            score = float(input("Enter score: "))
            add_course_and_score(students, student_id, course, score)
        elif choice == "3":
            student_id = input("Enter student ID: ")
            display_student_info(students, student_id)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
