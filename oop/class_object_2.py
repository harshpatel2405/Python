class Keyboard:
    def setData(self, name, price, company, type):
        self.name = name
        self.price = price
        self.company = company
        self.type = type

    def getData(self):
        print("Name :", self.name)
        print("Price :", self.price)
        print("Company :", self.company)
        print("Type :", self.type)


obj1 = Keyboard()
obj1.setData('HP Gaming', 1199, 'HP', 'Mechanical')
obj1.getData()

obj2 =  Keyboard()
obj2.setData("AntEsports 1200 mini",1499,'Ant E Sports','Normal')
obj2.getData()
