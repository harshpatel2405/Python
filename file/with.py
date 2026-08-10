with open("file6.txt",'w') as file:
    file.write("Hello\n")
    file.write("Hello\n")
    file.write("Hello\n")
    file.write("Hello\n")

# with open("file6.txt",'r') as file:
#     print(file.readlines())

with open("file6.txt",'r') as file:
    for line in file:
        print(line)