n = 10
eSum = 0
eCount = 0
oSum = 0
oCount = 0

print("EVEN", end="\t")
for i in range(1, n+1):
    if (i % 2 == 0):
        print(i, end="\t")
        eSum += i
        eCount += 1
print("Sum =", eSum, "\tCount :", eCount)

print("Odd\t", end="")
for i in range(1, n+1):
    if (i % 2 != 0):
        print(i, end="\t")
        oSum += i
        oCount += 1
print("Sum =", oSum, "\tCount :", oCount)
