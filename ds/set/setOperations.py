parent = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100}
a = {10, 20, 30, 40}
b = {10, 20, 50, 60}

# * union
c = a | b
print("Union :", c)

# * intersection
c = a & b
print("Intersection :", c)

# * difference (elements only from first set)
c = a - b
print("Difference :", c)

# * symmetric difference
c = a ^ b
print("Symmetric Difference :", c)

# *** Comparison Methods ***
a = {10, 20}
b = {30,40}

print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b)) # * returns true when no elements are common

# * inbuilt methods
print(max(parent))
print(min(parent))
print(sum(parent))
print(len(parent))