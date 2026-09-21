from . import database

id = 0


def addStudent():
    global id
    name = input("Enter Name : ")
    age = input("Enter age : ")
    email = input("Enter email : ")
    id += 1
    database.add_data(id, name, age, email, "student")


def getAllStudent():

    students = database.getAllData("student")

    if not students:
        print("\nNo students found.")
        return

    print("\n" + "=" * 80)
    print("|" + " STUDENT LIST ".center(78) + "|")
    print("=" * 80)

    print(f"| {'ID':<5}" f"| {'NAME':<20}" f"| {'EMAIL':<35}" f"| {'AGE':<5} |")

    print("-" * 80)

    for student in students:

        print(
            f"| {student['id']:<5}"
            f"| {student['name']:<20}"
            f"| {student['email']:<35}"
            f"| {student['age']:<5} |"
        )

    print("=" * 80)
