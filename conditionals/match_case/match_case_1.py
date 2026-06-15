a = int(input("1. Spring\n2. Summer\n3. Monsoon\n4. Winter\nEnter your favourite Season : "))

match a:
    case 1:
        print("Spring")
    case 2:
        print("Summer")
    case 3:
        print("Monsoon")
    case 4:
        print("Winter")
    case _:
        print("Enter choice between 1 and 4")
