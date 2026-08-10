f = open("file3.txt", 'w')

f.write("Harsh Patel\n")
f.write("Raviraj Bihola \n")
f.write("Jeel Parekh\n")
f.write("")
f.write("Bansari Patel\n")
f.write("Dhruv Patel\n")

f.close()

f = open("file3.txt", 'r')

# * Complete File Read

# print("Cursor Position : ", f.tell())

# print("Read 1 :", f.read())
# print("Cursor Position : ", f.tell())
# print("Read 2 :", f.read())
# print("Cursor Position : ", f.tell())

# * read specific number of characters
# print("File Read 7 : ",f.read(7))

# * read line
# print("Line 1 : ", f.readline())
# print("Line 1 : ", f.readline())
# print("Line 1 : ", f.readline())
# print("Line 1 : ", f.readline())
# print("Line 1 : ", f.readline())

while (True):
    line = f.readline()
    print(line)

    if (line == ''):
        break

f.close()
