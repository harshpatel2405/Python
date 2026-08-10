import os

if os.path.exists("file6.txt"):
    os.remove("file6.txt")
    print("File deleted")
else:
    print("File not found")