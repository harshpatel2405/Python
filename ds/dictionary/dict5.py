
# * nested dictionary
student = {
    101: {
        "name": "harsh",
        "age": 22
    },
    102:
    {
        "name": "Vasu",
        "age": 23
    }
}

print(student)
print(student[101])
print(student[101]["name"])

student = {
    "name": ['Harsh', 'Vasu', 'Dev'],
    "marks": [100, 99, 98],
    "age": [22, 23, 21]
}
print(student)
print(student["name"])
print(student["name"][0])


# * Practice 1
'''
1. Store 3 students 
2. print all names
3. calculate average marks 
4. find highest marks (student)
5. add one more student 
'''
student = {
    101: {
        "name": "Harsh",
        "age": 22,
        "marks": 89,
    },
    102: {
        "name": "Vasu",
        "age": 23,
        "marks": 79,
    },
    103: {
        "name": "Dev",
        "age": 21,
        "marks": 52,
    }
}
#  ^ print all names
# for key, values in student.items():
#     print(key, " -> ", values["name"])
for key in student:
    print(student[key]["name"])

# ^ calculate average marks
sum = 0
for key in student:
    sum += student[key]["marks"]

avg = sum / len(student)
print("Average Marks :", avg)

#  ^ find highest marks
max = 0
for key in student:
    if (max < student[key]["marks"]):
        # max = student[key]["marks"]
        max = key

# print("Maximum Marks =",max)
print("Maximum Data =", student[max])

# ^ add one more student
# student[104]= {
#     "name": "Krishna",
#     "age" :20,
#     "marks" : 45
# }

student.update({
    104: {"name": "Krishna",
          "age": 20,
          "marks": 45
          }
})

print(student)


# * list with dictionary
data = [
    {"name": "harsh", "age": 45}, {"name": "vasu",
                                   "age": 45}, {"name": "dev", "age": 45}
]
print(data[0]["name"])
