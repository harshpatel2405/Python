
##########################
# ^   *args -- works for n number of args   -gives tuple
def sum(*args):
    sum = 0
    for i in args:
        sum += i
    print(sum)


sum(10)
sum(10, 20)
sum(10, 20, 30)
sum(10, 20, 30, 40)

##########################
# ^  **kwargs -- works for n args , gives dictionary


def data(**kwargs):
    print(kwargs)


data(name='harsh', age=22)
a = ['harsh', 'vasu', 'dev']
b = [22, 23, 21]

data(name=a, age=b)
data(address={"pincode": 388620, "locality": "khambhat no dariyo"}, contactNo = 9876543201)
##########################
