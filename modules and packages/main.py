from school import student
from school import teacher
from school import database

n = -1

while n != 5:
    n = int(
        input(
            "1. Add A Student \n2. Add a teacher\n3. Get All Student\n4. Get All Teachers\n5. Exit\nSelect Your Operation : "
        )
    )

    match n:
        case 1:
            student.addStudent()
        case 2:
            teacher.addTeacher()
        case 3:
            student.getAllStudent()
        case 4:
            teacher.getAllTeacher()
        case _:
            print("Select Correct Input")
