import data
import functions

while True:
    a = int(input("1. add a student\n2. get all data\nSelect Correct Choice : "))
    match a:
        case 1:
            id = int(input("Enter id : "))
            name = input("Enter Name : ")
            functions.add_student(id, name, [10, 20, 30])
        case 2:
            data.getValues()
        case 3:
            break
