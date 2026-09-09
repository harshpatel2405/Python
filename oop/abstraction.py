
# *  implementation should be done by child class
from abc import ABC , abstractmethod

class Vehicle(ABC):
    
    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def show(self):
        print("Car class called")
        
    def start(self):
        print("Start method intialised")        
        
c =Car()
c.show()


from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


class UPI(Payment):

    def pay(self):
        print("Payment through UPI")


class CreditCard(Payment):

    def pay(self):
        print("Payment through Credit Card")


class NetBanking(Payment):

    def pay(self):
        print("Payment through Net Banking")
        
"Payment is only a blueprint/contract. You must create a specific payment type."