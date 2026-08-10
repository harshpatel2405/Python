f = open("data1.txt", 'w')

# * write into file
f.write('Hello World')
f.close()


f = open("data1.txt", 'r')
# * reads entire file
print("Complete File Data :", f.read())

f.close()
