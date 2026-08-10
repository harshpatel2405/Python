f = open("data2.txt", 'a')

f.write("Hello World\n")

f.close()

# * storing a variable in file
a = 100
f = open("data2.txt", 'w')
f.write(f"{a}")

f.close()

# * ask 3 names , age , marks from user and store it in file
f = open("data2.txt",'w')
for i in range(3):
    name = input("Enter name : ")
    age = int(input("Enter age : "))
    marks = int(input("Enter marks : "))

    f.write(f"{name}\t{age}\t{marks}\n")
f.close()