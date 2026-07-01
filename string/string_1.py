
#  * string is there , character is not there --
# * string is immutable -- cannot be modified/updated

name = "Harsh"
str = 'this is a single quote string '
str2 = '''This is also single string '''

# * printing strings
print(name)
print(str)
print(str2)

# * index access
print(name[2])
print(name[-1])

# * string concatenation
print("Harsh" + " Patel")
# print("Harsh" + 5)
# print(5 + "Harsh")
print("5" + "5")

# * repetition
print("hi" * 3)

# * length
print(len(name))

# * upper
print(name.upper())

# * lower
print(name.lower())

# * title -- capitalize first letter of each word
print(str.title())

# * capitalize -- capitailze the first character of the string
print(str.capitalize())


'''
1. Print the length of the string "Artificial Intelligence".
2. Find the length of your own name stored in a variable.
3. Convert the string "python" to uppercase.
4. Convert the string "JAVA" to lowercase.
5. Convert the string "welcome to python programming" to title case.
6. Convert the string "hello world" using the capitalize() method.
7. Store the string "machine learning" and print:
    Original string
    Uppercase
    Lowercase
    Title case
    Capitalized
8. Write a program to print the first and last character of a string entered by the user.
9. Write a program to concatenate two strings entered by the user.
10. Write a program to print a string 10 times using the repetition operator.
11. Write a program to count the number of characters in a user-entered string.
12. Write a program that converts a user's name to uppercase.
'''
'''7. Store the string "machine learning" and print:
    Original string
    Uppercase
    Lowercase
    Title case
    Capitalized
'''
str = "machine learning"
print("Original String :", str)
print("Uppercase String :", str.upper())
print("Lowercase String :", str.lower())
print("Title String :", str.title())
print("Capitalized String :", str.capitalize())


'''
8. Write a program to print the first and last character of a string entered by the user.
'''
str = input("Enter a string : ")
print(str[0])
print(str[-1])

'''
9. Write a program to concatenate two strings entered by the user.
'''
str1 = "harsh"
str2 = " patel"
print(str1+str2)


'''
10. Write a program to print a string 10 times using the repetition operator.
'''
str = "task"
print(str*10)

'''
11. Write a program to count the number of characters in a user-entered string. -- len 
12. Write a program that converts a user's name to uppercase.
'''
str = input("Enter your name : ")
print(str.upper())
