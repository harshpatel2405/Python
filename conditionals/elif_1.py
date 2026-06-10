'''
Input marks and print grades:
	≥90 → Grade A
	75–89 → Grade B
	50–74 → Grade C
	<50 → Grade D
'''

marks = int(input("Enter your marks : "))

if (marks >= 90):
    print("Grade A")
elif (marks >= 75 and marks <= 89):
    print("Grade B")
elif (marks >= 50 and marks <= 74):
    print("Grade C")
else:
    print("Grade D")
