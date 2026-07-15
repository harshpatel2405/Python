'''
len


'''

num = [10, 20, 30, 40, 50]
print("Length :", len(num))
print(max(num))
print(min(num))
print(sum(num))

# * substring
print(num[:4])
print(num[1:4])
print(num[1:4:2])
print(num[1::])
print(num[:: 4])
print(num[:: -1])

# * list comprehension
ans = [x for x in range(10)]
print(ans)

ans = [x for x in range(1, 11) if x % 2 == 0]
print(ans)

ans = ['Even' if x % 2 == 0 else 'odd' for x in range(1, 10)]
print(ans)

fruits = ['Apple','Banana','Chikoo','Mango']
upperCase_fruits = []

for x in fruits:
    if 'a' in x.lower():
        upperCase_fruits.append(x.upper())

print(upperCase_fruits)

fruits = ['Apple','Banana','Chikoo','Mango']
upperCase_fruits = [x.upper() for x in fruits if 'a' in x.lower()]
print(upperCase_fruits)

# * Replace List’s Item with New Value if Found

'''
INPUT :  10 20 30 40 50
enter which element to change : 40
element found 
enter new value : 99 
value updated

10 20 30 99 50
'''

'''
 Reverse Every Word
    Given
    words = ["apple", "banana", "orange"]

    Output
    ["elppa", "ananab", "egnaro"]

'''
words = ["apple", "banana", "orange"]

for word in words:
    print(word[::-1])

str = 'Python is easy and Python is powerful'.split()
unique_Word = []

for i in str:
    if i not in unique_Word:
        unique_Word.append(i)

print(unique_Word)

for word in unique_Word:
    count = 0
    for i in str:
        if(i == word):
            count+=1
    print(word,":",count)