
# * Enter a country code:   nested match case
# *    1. India
# *    2. USA
# *    3. UK
# *    Then enter a city code (use nested switch):
# *    - India → 1. Delhi, 2. Mumbai
# *    - USA   → 1. New York, 2. Texas
# *    - UK    → 1. London, 2. Manchester

country = int(input("1. India\n2. USA\n3. UK\nSelect Your Country : "))

match country:
    case 1:
        state = int(input("1. Delhi\n2. Mumbai\nSelect your State : "))

        match state:
            case 1: print("INDIA - Delhi")
            case 2: print("INDIA - Mumbai")
            case _: print("INDIA - Unknown State")

    case 2:
        state = int(input("1. New York\n2. Texas\nSelect your State : "))
        match state:
            case 1: print("USA - New York")
            case 2: print("USA - Texas")
            case _: print("USA - Unknown State")

    case 3:
        state = int(input("1. London\n2. Manchester\nSelect your State : "))
        match state:
            case 1: print("UK - London")
            case 2: print("UK - Manchester")
            case _: print("UK - Unknown State")

    case _:
        print("Select Correct Country")
