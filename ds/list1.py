user = ['Apple', 'Harsh', 'Vasu', 'Dev', 'Kirtan', 'Sujal', 'Vaibhav']
print(user)

print(user[0])

# * append
user.append("zaid")
print(user)

new_names = ['Apple', 'Banana', 'Mango']
# user.append(new_names)
# print(user)

#  * extend
user.extend(new_names)
print(user)

# * index
print(user.index('Apple'))
# print(user.index('Apples')) #* returns value error if not found

# * insert
user.insert(2, 'Blueberry')
print(user)

#  * count
print(user.count('Apple'))

#  * 
user.pop()
print(user)

#  * user.remove
user.remove('Apple')
print(user)


print(user.clear())

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 78.98, True]
print(data)
