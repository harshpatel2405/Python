class Car:
    def getData(self):
        self.a = 89
        print("Value of a is", self.a)


obj1 = Car()
obj1.getData()

'''
self -- makes a relation to the current object
'''


class Person:
    def setData(self):
        self.name = "harsh"
        self.age = 22
        self.address = "Ghar"

    def getData(self):
        print("Name :", self.name)
        print("Age :", self.age)
        print("Address :", self.address)
        if (self.age > 18):
            print("You Can Vote")
        else:
            print("You cannot vote")

obj = Person()
obj.setData()
obj.getData()
