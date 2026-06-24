
import math as m
n = 1234
# * digits - 4 3 2 1
sum = 0
mul = 1

while (n > 0):
    ld = n % 10
    print(ld)
    sum += ld
    mul *= ld

    if (ld % 2 == 0):
        print("Even -", ld)
    else:
        print("ODD -", ld)
    n = n // 10

print("Sum :", sum)
print("Multiplication :", mul)


# * FACTORIAL OF ALL DIGITS
n = 7895
while (n > 0):
    ld = n % 10
    factorial = m.factorial(ld)
    print(f"{ld}! = {factorial}")
    n //= 10


# * reverse of number
n = 12321
rev = 0
while (n > 0):
    ld = n % 10
    rev = rev * 10 + ld
    n //= 10

print(rev)

# * palindrome -- reverse of the number ===  original number
n = 12321
temp = n
rev = 0
while (n > 0):
    ld = n % 10
    rev = rev * 10 + ld
    n //= 10

if (temp == rev):
    print(f"{temp} is palindrome")
else:
    print(f"{temp} is not palindrome")

# * armstrong number
# ^ 153 = 1^3 + 5^3 + 3^3 (3 is number of digits)
n = 1534

temp = n
count = 0
#  & find number of digits
while (n > 0):
    count += 1
    n //= 10

n = temp
armstrong = 0
while (n > 0):
    ld = n % 10
    power = m.pow(ld, count)
    armstrong += power
    n = n // 10

if (temp == armstrong):
    print(f"{temp} is armstrong")
else:
    print(f"{temp} is not armstrong")

# * krishnamurthy
# ^ 145 = 1! + 4! + 5! = 145