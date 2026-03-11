option = ""
students = []

notas = []

print("Hello dear user, Welcome to system of register students and notes :). \n")

while option != "5":
        print("""
Tienes 4 opciones
1. Register student.
2. Show list of students.
3. Enter new subjets.
4. Register note.
5. Exit the program.
""")
        option = (input("Enter a opcion to select: "))
        print()

        if option == "1":
            students_quantity = int(input("User please, enter a quantity students for register: "))

            for i in range(students_quantity):
                first_name = input(f"Enter a first name {i + 1}: ")
                middle_name = input(f"Enter a middle name {i + 1}: ")
                last_name = input(f"Enter a last name {i + 1}: ")
                second_last_name = input(f"Enter a second last name {i + 1}: ")
                print("")

                student = {
                    "first_name": first_name,
                    "middle_name": middle_name,
                    "last_name": last_name,
                    "second_last_name": second_last_name,
                    "subjects" : []
                }

                students.append(student)

        elif option == "2":

            print("\nStudents register: \n")
            for i, student in enumerate(students):
                    full_name = (f"{(student['first_name'])} {(student['middle_name'])} {(student['last_name'])} {(student['second_last_name'])}")

                    for i, subject in enumerate(student["subjects"]):
                        students_subjects = (f"{(student['subject_describe'])}")
                        print(f"{i + 1} Student: {full_name} | Subjects {students_subjects} \n")
        
        elif option == "3":

            subject_index = int(input("Select the student number: "))     
               
            subjects_quantity = int(input("How many subjets you want for student?: "))
            print("")

            for i in range(subjects_quantity):
                 subject_describe = input(f"Enter a subject for student {i + 1}: ")
                 print("")

                 subject = {
                      "subject_describe" : subject_describe
                 }

                 students[subject_index - 1]['subjects'].append(subject)
                
        else:
             print("I don't understand the option.")

  




