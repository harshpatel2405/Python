'''
Employee Salary Slip Simulation	Input:
	Basic Salary
	If salary > 20000
		HRA = 25%, DA = 90%
	Else
		HRA = 20%, DA = 80%
	Calculate and print Gross Salary
'''
basicSalary = int(input("Enter your salary : "))
hra = 0
da = 0

if (basicSalary > 20000):
    hra = 25
    da = 90
else:
    hra = 20
    da = 80

print("HRA = ", (hra * basicSalary) / 100)
print("DA = ", (da * basicSalary) / 100)

total = (hra * basicSalary) / 100 + (da * basicSalary) / 100 + basicSalary
print("Gross Salary :",total)