print("Start of the code")

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))

try:
    print("Inside Try :", a / b)
except ZeroDivisionError:
    print("Inside Except : Division by zero not possible")
else:
    print("Division Successfully executed")

print("End of the code")
