num = {10,20,30}

# * add
num.add(23)
print(num)

# * update 
num.update([11,12])
print(num)

# * remove
# num.remove(99) * KeyError: 99
print(num)

# *  discard
num.discard(99)
print(num)

# * pop
x = num.pop()
print(x)
print(num)

# * clear
num.clear()
print(num)
