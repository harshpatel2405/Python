file = open("file5.txt",'w+')

print("Cursor Position : ",file.tell())
file.write("Hello World")
print("Cursor Position : ",file.tell())

file.seek(10)
print("Cursor Position : ",file.tell())

print(file.read())
print("Cursor Position : ",file.tell())

file.close() 