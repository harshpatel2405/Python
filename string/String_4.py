
#  * index access , slicing  , repetion
# * length
# * split
# * count
# * find
# * rfind
# * title
# * upper
# * lower
# * capitalize

str = "demostrin44g"
# * charAt
#  * at

print(str.isalnum())  # checks whether string has both digits and alphabets
print(str.isalpha())  # checks whether all characters are alphabets or not
print(str.isdigit())
print(str.isupper())
print(str.islower())
print(str.isspace())

print(str.strip(), end=" . ")
print(str.lstrip(), end=" . ")
print(str.rstrip(), end=" . ")

print(str.index('d'))
print(str.replace('em','qp'))

print(str.startswith('d'))
print(str.endswith('g'))

print(str.zfill(30))

print(str.center(19 , '#'))
print(str.ljust(19 , '#'))
print(str.rjust(19 , '#'))


