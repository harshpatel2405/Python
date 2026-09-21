student_data = []
teacher_data = []


def add_data(id, name, age, email, role):
    create_data = {}
    create_data["id"] = id
    create_data["name"] = name
    create_data["age"] = age
    create_data["email"] = email
    if role == "student":
        student_data.append(create_data)
        print("student with id", id, "added successfully to database")
    else:
        teacher_data.append(create_data)
        print("teacher with id", id, "added successfully to database")


def getAllData(role):
    if role == "student":
        return student_data
    else:
        return teacher_data
