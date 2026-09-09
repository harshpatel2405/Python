class Animal:
    def show(self):
        print("Animal makes sound")
    
class Dog(Animal):
    def show(self):
        print("Dog Barks")
        
d = Dog()
d.show()


# operator overloading 
class Number:
    def __init__(self , value):
        self.value = value

    def __add__(self , other):
        return (self.value + other.value)

n1 = Number(10)
n2 = Number(20)
print(n1+n2)