student = {
    "name": "ram",
    "age": 21,
    "marks": 45
}

print("Student :", student)
# * access
print("Student Name :", student["name"])

# * add a new element 
student["address"] = "xyz"
print("Student :", student)

# * update 
student["age"] = 78
print(student)


# * delete any element
del student["age"]
print(student)

# * length
print("Length :", len(student))


# * if key is present in dictionary or not 
if "name" in student:
    print("Name is present")

# * traverse in dictionary 
for key in student:
    print("Key :", key, "\tValue :", student[key])

# * complete delete 
del student
# print(student)
