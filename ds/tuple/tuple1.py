num = ()
print(num)
print(type(num))

# * with paranthesis
num = (10,20,3,40.23)
print(num)

# * without paranthesis
num = 10 ,20,30,40
print(num)

num=(10, )
print(num)


num = 11,22,33,44,55
print(num[0])
# print(num[9]) #* IndexError: tuple index out of range
print(num[-1])

# num[0] = 101 # *TypeError: 'tuple' object does not support item assignment
# print(num)