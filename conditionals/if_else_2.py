'''
 A number is lucky if:
        Greater than 100    
        Less than 1000  
        Last digit is 7
'''

num = int(input("Enter a number : "))

if(num > 100 and num < 1000 and num % 10 == 7):
    print(f"{num} is lucky number")
else:
    print(f"{num} is not lucky number")