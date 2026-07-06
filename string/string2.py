# # slicing
# #      01234567890123456
# str = "Chess-sudoku-Ludo"

# print(str.split(" "))
# print(str.split())
# print(str.split("s"))
# # 'Che'','',
# #

# # * join

# print(str[1:3])
# print(str[3: 1:-1])
# print(str[1: 9:2])
# print(str[1:: 5])

# # *count  -- will return occurence of that particular element
# print(str.count('do'))

# # * find -- returns first index of occurence  - starts from left
# print(str.find("do"))

# # * rfind
# print(str.rfind("do"))

# '''
# 1. Student Information Formatter
# --------------------------------
# Accept the following details from the user:
# - Full Name
# - Course Name
# - City

# Perform the following operations:
# • Convert the full name to uppercase.
# • Convert the course name to lowercase.
# • Capitalize the city name.
# • Count the total number of characters in the full name (excluding spaces).
# • Display the formatted information in a proper format.
# '''


# name = input("Enter full name : ")
# course = input("Enter course name : ")
# city = input("Enter city : ")

# print("full Name :", name.upper())
# print("course    :", course.lower())
# print("city      :", city.capitalize())

# count = 0
# for i in name:
#     if (i == " "):
#         continue
#     count += 1
# print(count)

# count = 0
# for i in range(len(name)):
#     if(name[i] == " "):
#         continue
#     count+=1
# print(count)

'''
Name Formatter
-----------------
Accept a full name from the user.

Display:
• First Name
• Middle Name (if available)
• Last Name
• Initials
• Name in Title Case
• Name without spaces

Example:
Input:
Rahul Kumar Sharma

Output:
First Name : Rahul
Middle Name : Kumar
Last Name : Sharma
Initials : R.K.S.

Methods:
split(), title(), replace()

'''
name = input("Enter your full name : ")

print("First name : ", end="")
index = 0
for i in range(len(name)):
    if (name[i] == " "):
        index = i
        break
    print(name[i], end="")

print("\nMiddle Name : ", end="")
for j in range(index+1, len(name)):
    if (name[j] == " "):
        index = j
        break
    print(name[j], end="")

print("\nLast Name : ", end="")
for j in range(index+1, len(name)):
    if (name[j] == " "):
        index = j
        break
    print(name[j], end="")

print("\nInitials : ", end="")
print(name[0], end=".")
for i in range(len(name )):
    
    if(name[i] == " "):
        print(name[i+1] , end=".")