
# * shallow copy -- only assigned items gets changed

data = {
    101: "tv"
}

data1 = data.copy()
print(data1)

data1[102] = "phone"
print(data)
print(data1)

import copy

data = {
    101: "tv",
    102: ["phone", "watch", "toaster"]
}

data1 = copy.deepcopy(data)

data1[102][0] = 154

print(data)
print(data1)

