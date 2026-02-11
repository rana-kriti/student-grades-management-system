import time
students={  }

def add_student(name,grade):
    students[name]=grade
    print(f"Record of Student {name} with grade {grade} has been added.\n")

def update_student(name,grade):
    if name in students:
        students[name]=grade 
        print(f"Student {name} with marks are updated {grade}.\n")

    else:
        print(f"Student {name} is not found!\n")

def delete_student(name):
    if name in students:
        del students[name]
        print(f"Record of Student {name} has been deleted.\n")
    else:
        print(f"Student {name} is not found!\n")

def display_all_students():
    if students:
        for key, value in students.items():
            print(key, ":", value)
            time.sleep(1) 

    else:
        print("No students found/added\n")

# def class_statistics():
#     if students:
#         grades = [float(grade) for grade in students.values()]
#         print(f"Class Average: {sum(grades)/len(grades):.2f}")
#         print("Highest Grade:", max(grades))
#         print("Lowest Grade:", min(grades))
#     else:
#         print("No students added yet.")


welcome_text=("___Student Grades Management System___")
for char in welcome_text:
    print(char, end="", flush=True)
    time.sleep(0.05)
print("\n")

def main():
    while True:
        print("\n-----Functions for Student\'s list:----\n")
        
        menu = {
            1: "Add Student",
            2: "Update Student Record",
            3: "Delete Student Record",
            4: "Search Student Record",
            5: "View Students Profile",
            6: "View Class Statistics",
            7: "Exit"
        }
        for key, value in menu.items():
            time.sleep(0.5)
            print(f"{key}. {value}")

        choice = int(input("Enter your choice = "))

        if choice == 1:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            add_student(name,grade)

        elif choice == 2:
            name = input("Enter student name: ")
            grade = input("Enter student grade: ")
            update_student(name,grade)

        elif choice == 3:
            name = input("Enter student name: ")
            delete_student(name)

        elif choice == 4:
            search=input("Enter the student name to search: ")
            if search in students:
                print(f"The Student \"{search}\" is found.")
                print("Grade: ",students.get(search))
                for key, value in students.items():
                    time.sleep(0.5)
                    print(f"{key}: {value}")
            else:
                print("Data not found!")

        elif choice == 5:
            display_all_students()
            print("Length of the Student\'s list: ",len(students))

        elif choice == 6:
            print("Closing the program...")
            break

        else:
            print("Invalid choice!")



main() 