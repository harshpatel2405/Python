'''
Question 1 – Student Marks Update (Mid)

A school stores each student's details as a tuple.

students = [
    ("Harsh", (78, 85, 91)),
    ("Rahul", (67, 72, 80)),
    ("Priya", (88, 90, 95))
]
Requirements
Find the student "Rahul".
Increase every subject mark by 5.
Marks cannot exceed 100.
Convert the updated marks back into a tuple.
Print the updated list.
'''
students = [
    ("Harsh", (78, 85, 91)),
    ("Rahul", (67, 72, 80)),
    ("Priya", (88, 90, 96))
]

updatedStudents = []

for student in students:
    if("Rahul" == student[0]):
        print("Rahul found")


    data = list(student[1])
    for i in range(len(data)):
        data[i] = min(data[i] + 5, 100)

    data = tuple(data)

    student = (student[0], data)
    updatedStudents.append(student)

print(updatedStudents)