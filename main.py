students = []

print("Hello dear user, Welcome to system of register students and notes :). \n")



students_quantity = int(input("User please, enter a quantity students for register: "))
print("")


for i in range(students_quantity):
    first_name = input(f"Enter a first name {i + 1}: ")
    middle_name = input(f"Enter a middle name {i + 1}: ")
    last_name = input(f"Enter a last name {i + 1}: ")
    second_last_name = input(f"Enter a second last name {i + 1}: ")
    print("")

    student = {
        "first_name" : first_name,
        "middle_name" : middle_name,
        "last_name" : last_name,
        "second_last_name" : second_last_name
    }
    students.append(student)

print("\nStudents register: \n")
for i, student in enumerate(students):
    full_name = (f"{(student['first_name'])} {(student['middle_name'])} {(student['last_name'])} {(student['second_last_name'])}")
    print(f"{i + 1} Student: {full_name} \n")
