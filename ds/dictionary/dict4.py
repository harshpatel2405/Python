numbers = {}
for i in range(1, 6):
    numbers[i] = i*i
    print(i, "->", numbers[i])

numbers = {i: i*i for i in range(1, 6)}
print(numbers)

names = ["Krishna", "Madhav", "Gopal"]
name_length = {name: len(name) for name in names if name != 'Krishna'}
print(name_length)


# * swap key and value
data = {
    "name": "harsh",
    "age": 22,
    "marks": "Sauthi Vadhare"
}
new_data_swap = {value:key for key , value in data.items()}
print(new_data_swap)
