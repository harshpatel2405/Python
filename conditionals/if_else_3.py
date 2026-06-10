'''
Check whether the year entered by user is leap year or not 
    Leap Year Conditions:
        . Divisible by 400 → Leap Year
        . Else Divisible by 100 → Not Leap Year
        . Else Divisible by 4 → Leap Year
        . Else → Not Leap Year
'''
year = int(input("Enter a year : "))

if (year % 400 == 0):
    print("Leap Year")
elif (year % 100 == 0):
    print("Not Leap year")
elif (year % 4 == 0):
    print("Leap Year")
else:
    print("Not Leap year")
