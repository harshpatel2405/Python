
# * Task 1 : convert all elements of list into uppercase
# names = ['Harsh', 'Jeel', 'Raviraj', 'Dhruv', 'Bansari']

# for i in names:
#     print(i.upper())


# * Task : make a list of fruits 
# * 1. convert all fruit names to uppercase
# * 2. convert all fruits names to lowercase
# * 3. remove last fruits from the list 
# * 4. add 'Chikoo' in the fruits  

# * INPUT : ['Apple','Banana','Mango']
'''
1. APPLE BANANA MANGO
2. apple banana mango
3. Apple Banana
4. Apple Banana Chikoo
'''

'''
Student Attendance

You are given a list of student names.

students = ["Harsh", "Amit", "Priya", "Neha", "Rohan"]

Ask the user to enter a name.
Print "Present" if the name exists in the list, otherwise print "Absent".
'''

students = ["Harsh", "Amit", "Priya", "Neha", "Rohan"]

name = input("Enter your name : ")

if name in students:
    print("Present")
else:
    print("Absent")

'''
Store a list of email addresses.

Print only the usernames.
'''

emails = [
    "john@gmail.com",
    "alice@yahoo.com",
    "harsh@gmail.com"
]

for i in emails:
    # print(i[0:i.find('@')])
    print(i.split('@')[0])