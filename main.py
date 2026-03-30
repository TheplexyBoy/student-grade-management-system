# List to store all students
students = []

# Automatic ID counter
student_id_counter = 1


# Function to create a new student
def create_student():
    global student_id_counter

    # Ask user for student data
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))

    # Create student dictionary with automatic ID
    student = {
        "id": student_id_counter,
        "name": name,
        "age": age
    }

    # Add student to the list
    students.append(student)

    # Increase ID counter for next student
    student_id_counter += 1

    print("Student successfully registered")


# Function to display all students
def show_students():
    # Check if the list is empty
    if not students:
        print("No students registered")
        return

    # Loop through the list and print each student
    for s in students:
        print(f'ID: {s["id"]} | Name: {s["name"]} | Age: {s["age"]}')


# Function to delete a student by ID
def delete_student():
    # Ask for the ID to delete
    student_id = int(input("Enter student ID to delete: "))

    # Search for the student
    for s in students:
        if s["id"] == student_id:
            students.remove(s)
            print("Student deleted successfully")
            return

    # If ID was not found
    print("Student ID not found")


# Function to edit student data
def edit_student():
    # Ask for the ID to edit
    student_id = int(input("Enter student ID to edit: "))

    # Search for the student
    for s in students:
        if s["id"] == student_id:

            print("Leave blank if you do not want to change a field")

            # Ask for new values
            new_name = input("New name: ")
            new_age = input("New age: ")

            # Update only if values are provided
            if new_name != "":
                s["name"] = new_name

            if new_age != "":
                s["age"] = int(new_age)

            print("Student updated successfully")
            return

    # If ID was not found
    print("Student ID not found")


# Main menu loop
while True:
    print("\n--- STUDENT REGISTRATION SYSTEM ---")
    print("1. Register student")
    print("2. Show students")
    print("3. Delete student")
    print("4. Edit student")
    print("5. Exit")

    option = input("Choose an option: ")

    if option == "1":
        create_student()

    elif option == "2":
        show_students()

    elif option == "3":
        delete_student()

    elif option == "4":
        edit_student()

    elif option == "5":
        print("Exiting system")
        break

    else:
        print("Invalid option")
