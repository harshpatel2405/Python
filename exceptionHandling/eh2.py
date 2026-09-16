print("Start of Code")

a = input("Enter a number : ")
# a = int(input("Enter a number : "))
try:
    print("Inside Try :", 10 / a)
except TypeError:
    print("Inside Except : TypeError : ", TypeError)
except ZeroDivisionError as ze:
    print("Inside Except :  ZeroDivisionError : ", ze)
finally:
    print("Finally Executed")

print("End of Code")
