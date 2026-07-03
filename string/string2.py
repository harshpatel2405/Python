# slicing
#      01234567890123456
str = "Chess-sudoku-Ludo"

print(str.split(" "))
print(str.split())
print(str.split("s"))
# 'Che'','',
#

# * join

print(str[1:3])
print(str[3: 1:-1])
print(str[1: 9:2])
print(str[1:: 5])

# *count  -- will return occurence of that particular element
print(str.count('do'))

# * find -- returns first index of occurence  - starts from left
print(str.find("do"))

# * rfind
print(str.rfind("do"))

