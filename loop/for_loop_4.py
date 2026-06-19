
# * string -> array / collection of characters
name = input("Enter a string : ")

# * 1. Print each character on a same line
for i in name:
    print(i, end="")

print()
# * 2. Print characters with index (len)
length = len(name)  # * will give number of characters stored in the name

for i in range(length):  # * 0 to length-1
    # * i is index and name[i] is character at that index
    print(i, " -", name[i])

#  * 3.  Count total characters without using len()
count = 0
for i in name:
    count += 1

print("Total Characters :", count)


# * 4. Print string in reverse   (Harsh -> hsraH)
#  range(start, stop , step)
#  range(4,-1,-1)
for i in range(len(name)-1, -1, -1):
    print(name[i])

# * 5. Check whether a character exists
#  * Name= Harsh (Is r present in Harsh -> true)
target = 'r'
for i in name:
    if (i == target):
        print("Element Found")
        break

# * 9. Count occurrences of a character
# * 10. First occurrence position
# * 11. Last occurrence position