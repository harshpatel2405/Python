'''
Enter number of working days and days present; calculate attendance %:
	≥ 90% → Excellent
	75–89% → Good
	50–74% → Average
	< 50% → Poor
'''
workingDays = int(input("Enter number of working days : "))
presentDays = int(input("Enter number of days you were present : "))

percentage = presentDays / workingDays * 100
print("Percentage :", percentage)

if (percentage >= 90):
    print("Excellent")
elif (percentage >= 75 and percentage <= 89):
    print("Good")
elif (percentage >= 50 and percentage <= 74):
    print("Average")
elif (percentage < 50):
    print("Poor")
