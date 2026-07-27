data = {
    "name": "Harsh",
    "name": "harsh",
    "marks" : 44,
    "age": 22,
}
print(data)

# * pop -- removes with key
data.pop("name")
print(data)

# * popitem -- removes last inserted data 
data.popitem()
print(data)

# * clear -- clears data from dictionary
data.clear()
print(data)


info = {
    True : 45,
    2.2 : "Harsh"
}
print(info[True])