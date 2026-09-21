from . import database

id = 0


def addTeacher():
    global id
    name = input("Enter Name : ")
    age = input("Enter age : ")
    email = input("Enter email : ")
    id += 1
    database.add_data(id, name, age, email, "teacher")


def getAllTeacher():

    teachers = database.getAllData("teacher")

    if not teachers:
        print("\nNo teachers found.")
        return

    print("\n" + "=" * 75)
    print("                         TEACHER LIST")
    print("=" * 75)

    print(f"{'ID':<5}" f"{'NAME':<20}" f"{'EMAIL':<35}" f"{'AGE':<5}")

    print("-" * 75)

    for teacher in teachers:

        print(
            f"{teacher['id']:<5}"
            f"{teacher['name']:<20}"
            f"{teacher['email']:<35}"
            f"{teacher['age']:<5}"
        )

    print("=" * 75)
