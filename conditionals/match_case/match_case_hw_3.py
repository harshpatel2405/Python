'''
3.  Menu-driven program:
   1. Area of Circle
   2. Area of Rectangle
   3. Area of Triangle
   4. Exit
'''


choice = int(input(
    " 1. Area of Circle\n2. Area of Rectangle\n3. Area of Triangle\n4. Exit\nSelect your choice : "))

match choice:
    case 1:
        print("AREA OF CIRCLE  =   pi * r * r")
        r = int(input("Enter radius : "))
        area = 3.14 * r * r
        print(f"Area of Circle wirth radius {r} cm is {area} cm2")

    case 2:
        print("AREA OF RECTANGLE = length * breadth")
        length = int(input("Enter length : "))
        breadth = int(input("Enter breadth : "))
        area = length * breadth
        print(
            f"Area of Rectangle with length {length} cm and breadth {breadth} cm is {area} cm2")

    case 3:
        print("AREA OF TRIANGLE = (base * altitude) / 2")
        base = int(input("Enter base : "))
        altitude = int(input("Enter altitude : "))
        area = base * altitude / 2
        print(
            f"Area of Triangle with base {base} cm and altitude {altitude} cm is {area} cm2")

    case 4:
        print("Exiting the menu driven program")
    case _:
        print("enter between 1 and 4 only")
