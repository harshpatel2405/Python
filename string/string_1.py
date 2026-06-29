
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
