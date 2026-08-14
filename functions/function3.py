# #############################
# * lambda
def result(x): return x*x


print("Result :", result(7))


def result(a, b): return a+b


print("Result :", result(10, 30))


def result(a, b): return print(a+b)


result(10, 30)


num = [10, 20, 30, 40]

result = list(map(lambda x: x*x, num))
print(result)


num = [10, 20, 30, 40,11,22,33,44,55]

result = list(filter(lambda x: x%2 ==0, num))
print(result)