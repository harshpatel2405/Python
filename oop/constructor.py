class Keyboard:
    def __init__(self, name, price, company, type):
        self.name = name
        self.price = price
        self.company = company
        self.type = type

    def getData(self):
        print("Name :", self.name)
        print("Price :", self.price)
        print("Company :", self.company)
        print("Type :", self.type)


obj1 = Keyboard('HP Gaming', 1199, 'HP', 'Mechanical')
obj1.getData()

obj2 =  Keyboard("AntEsports 1200 mini",1499,'Ant E Sports','Normal')
obj2.getData()

'''
# Employee Salary Management

Create a class `Employee` with:

* `employeeId`
* `name`
* `basicSalary`
* `bonus`

## Requirements

* Use a **parameterized constructor** to initialize the employee.
* Create a function `calculateSalary()` that returns `basicSalary + bonus`.
* Create a function `display()` to print all employee details.
* Create **at least 3 employee objects**.
'''
