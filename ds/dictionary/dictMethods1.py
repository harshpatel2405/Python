food ={
    "fruit" : "Apple",
    "vegetable" : "Potato",
    "pulse" : "Mung",
    "budget" : 50000,
}

# * get -- key
ans1 = food.get("fruit")
print(ans1)

# * keys -- returns all key of dictionary -- ([])
ans2 = food.keys()
print(ans2)

# * values -- returns all values from dictionary -- ([])
ans3= food.values()
print(ans3)

for value in food.values():
    print(value)

# * items -- returns all pairs 
ans4 = food.items()
print(ans4)

# * iterating in food
for i in food.items():
    print(i[0],"->",i[1])

for key , value in food.items():
    print(key,"->",value)

# * update 
food.update({
    "fruit":"Banana",
    "protein" : "paneer"
})
print(food)

# * fromKeys -- make dictionary 
key = ["name","age","marks"]
d = dict.fromkeys(key,"Harsh")
print(d)

# * len , max, min , type
print(max(food))
print(min(food))


