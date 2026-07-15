'''
File Extension Counter

Given

files = [
    "photo.jpg",
    "resume.pdf",
    "movie.mp4",
    "image.jpg",
    "notes.pdf",
    "python.py"
]

Count how many files belong to each extension.
'''

files = [
    "photo.jpg",
    "resume.pdf",
    "movie.mp4",
    "image.jpg",
    "notes.pdf",
    "python.py"
]
file_extension = []
for file in files:
    if (file.split(".")[1] not in file_extension):
        file_extension.append(file.split(".")[1])

print(file_extension)

for ext in file_extension:
    count = 0
    for file in files:
        curr = file.split(".")[1]

        if(curr == ext):
            count+=1

    print(f"{ext} -> ({count})")
