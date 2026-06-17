'''
5. Create a currency converter using switch:
    1. INR to USD
    2. USD to EUR
    3. EUR to INR
'''

choice = int(
    input("1. INR TO USD\n2. USD TO EUR\n3. EUR TO INR\nSELECT YOUR CHOICE : "))
match choice:
    case 1:
        amount = int(input("Enter in Inr to convert in USD : "))
        print("95 rs = 1 USD")
        print(f"{amount} rupees = {amount/ 95} USD")

    case 2:
        amount = int(input("Enter in USD to convert in EUR : "))
        print("1 USD = 0.85 EUR")
        print(f"{amount} USD = {amount/ 0.85} EUR")
    case 3:
        amount = int(input("Enter in eur to convert in INR : "))
        print("1 EUR = 111 INR")
        print(f"{amount} EUR = {amount* 111} INR")
    case _:
        print("Enter correc operation")
