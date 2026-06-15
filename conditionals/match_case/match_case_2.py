
# * make an ATM
choice = int(input(
    "1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\nEnter your choice : "))
balance = 25000

match choice:
    case 1:
        amount = int(input("Enter amount to be depositted : "))
        balance += amount
        print(f"{amount} depositted Successfullly..Current Balance is {balance}")

    case 2:
        amount = int(input("Enter amount to be withdrawn : "))
        if (amount <= balance):
            balance -= amount
            print(f"{amount} Withdrawn Successfullly..Current Balance is {balance}")
        else:
            print("Insufficient Balance")

    case 3:
        print("Current Balance :", balance)

    case  4:
        print("Exiting the ATM")

    case _:
        print("Select Correct Choice")
