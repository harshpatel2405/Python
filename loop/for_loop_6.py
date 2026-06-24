'''
# * Left Aligned Right Angle Triangle
a
b b
c c c 
d d d d 
'''
n = 5
ch = 97  # * ascii of 'a'
for i in range(1, n+1):

    for j in range(1, i+1):
        print(chr(ch), end=" ")

    ch += 1
    print()
'''
# * Left Aligned Right Angle Triangle
a
a b
a b c 
a b c d 
'''
n = 5
for i in range(1, n+1):
    ch = 97  # * ascii of 'a'
    for j in range(1, i+1):
        print(chr(ch), end=" ")
        ch += 1
    print()

'''
# * Left Aligned Right Angle Triangle
a
b c 
d e f 
g h i j 
k l m n o
'''
n = 5
ch = 97  # * ascii of 'a'
for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(ch), end=" ")
        ch += 1
    print()
