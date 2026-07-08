
#  * encrypt and decrypt the password
SignupdatabasePassword = input("Enter the password : ")
SignupdatabasePassword = SignupdatabasePassword.strip()

# * encrypt
SignupdatabasePassword = SignupdatabasePassword.center(
    len(SignupdatabasePassword*2), '#')
print("Password Stored in database: ", SignupdatabasePassword)

loginPassword = input("Enter login password : ")
lPassword = ''
#  * decrypt
for ch in SignupdatabasePassword:
    if (ch == '#'):
        continue
    lPassword += ch

if (lPassword == loginPassword):
    print("Login Successfull")
else:
    print("Invalid credentials")
