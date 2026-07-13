'''
Student Result Analyzer

Store student records.

students = [
    "Harsh-85",
    "Amit-72",
    "Neha-91",
    "Jay-65"
]

Print only students scoring above 80.
Print avg of the marks of everyone 
'''
students = [
    "Harsh-85",
    "Amit-72",
    "Neha-91",
    "Jay-65"
]


sum = 0
for i in students:
    marks = int(i.split('-')[1])
    sum += marks

    if (marks > 80):
        print(i.split('-')[0])

avg = sum / len(students)
print(f"Average = {avg}")


'''
Chat Filter
Given
messages = [
    "Hello",
    "You are stupid",
    "Good Morning",
    "idiot",
    "Nice Work",
    "Stupid",
    "Rascal",
    "Handsome",
]
Create a list of banned words.
Replace inappropriate messages with

*****
'''

messages = [
    "Hello",
    "You are stupid",
    "Good Morning",
    "Idiot",
    "Nice Work",
    "Stupid",
    "Rascal",
    "Handsome",
]
inappropriateWords = ['stupid', 'rascal', 'idiot', 'donkey']

for i in messages:
    if i.lower() not in inappropriateWords:
        print(i, end=" ")
    else:
        # print('*****', end=" ")
        print('*' * len(i), end = " ")

