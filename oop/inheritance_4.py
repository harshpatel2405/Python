class Sugar:
    def show(self):
        print("Sugar class called")


class Water:
    def show(self):
        print("Water class called")


class Lemonade(Sugar, Water):
    def showLemonade(self):
        # super().show()
        # super().show()
        Sugar().show()
        Water().show()
        print("Lemonade class called")


obj1 = Lemonade()
obj1.showLemonade()
