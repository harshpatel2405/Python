'''
Question 1 – Common Subjects

Three students have selected different subjects.

student1 = {"Math", "Physics", "Python", "DBMS"}
student2 = {"Python", "Java", "Math", "AI"}
student3 = {"Python", "Math", "Cyber Security"}

Requirements:
    Display subjects common to all students.
    Display subjects selected by at least one student.
    Display subjects chosen by student1 but not by student2.
    Check whether student3's subjects are a subset of student1's subjects.
'''
'''
Question 1 – Student Sports Registration (Recommended ⭐)

A school stores the names of students who registered for two sports. Since some students registered multiple times by mistake, the data is stored in lists.

football = ["Harsh", "Rahul", "Priya", "Harsh", "Amit"]
cricket = ["Rahul", "Jay", "Priya", "Jay", "Karan"]
Requirements
    Remove duplicate names from both lists.
    Convert both lists into sets.
    Find students who registered for both sports.
    Find students who registered only for Football.
    Display all unique students.
'''
football = ["Harsh", "Rahul", "Priya", "Harsh", "Amit"]
cricket = ["Rahul", "Jay", "Priya", "Jay", "Karan"]


football = set(football)
print("Football :", football)
cricket = set(cricket)
print("Cricket :", cricket)

print("Students Registerd in Cricket and Football :", football & cricket)
print("Students Registerd only in Football :", football - cricket)
print("Students unique :", football ^ cricket)
