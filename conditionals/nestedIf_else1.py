'''
Voter Eligibility with Age Check		
Ask user age:
	If age ≥ 18
		If age ≥ 60 → "Senior Citizen Voter"
		Else → "Regular Voter"
	Else → "Not Eligible to Vote"
'''

age = int(input("Enter your age : "))

if (age >= 18):
    if (age >= 60):
        print("Senior Citizen")
    else:
        print("Regular Voter")
else:
    print("Not eligible to vote")
