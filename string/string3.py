
# * Ask a password from user , and check this five conditions
# *  1. it should contain atleast one uppercase character
# *  2. it should contain atleast one lowercase letter
# *  3. It should contain atleast one digit
# *  4. it should contain atleast one special character
# *  5. Minimum length should be 8 and max length should be less than 16
password = input("Enter the password : ") 

# special_chars = '!@#$%^&*()_+{}|[]\:;,./<>?~`'
upper = False
lower = False
digit = False
special = False

if (len(password) >= 8 and len(password) <= 16):
    for ch in password:
        if (ch.isupper()):
            upper = True
        elif (ch.islower()):
            lower = True
        elif (ch.isdigit()):
            digit = True
        elif not (ch.isalnum()): # else 
            special = True

    if (upper and lower and digit and special):
        print("Strong Password")
    else:
        print("Password is Weak(try to satisfy all the conditions )")

else:
    print("Password should be betweeen 8 and 16 characters")


# * Task : check whether the character entered by the user is special character or not 