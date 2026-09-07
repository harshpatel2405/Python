class Pizza:
    def showPizza(self):
        print("Pizza class called")
    
class VegPizza(Pizza):
    def showVegPizza(self):
        super().showPizza()
        print("Veg Pizza class called")
    
class CheesePizza(Pizza):
    def showCheesePizza(self):
        super().showPizza()
        print("Cheese Pizza class called")

obj1 = VegPizza()
obj1.showVegPizza()

obj2 = CheesePizza()
obj2.showCheesePizza()
    
    # 1 parent , N child   hierarchical INHERITANCE