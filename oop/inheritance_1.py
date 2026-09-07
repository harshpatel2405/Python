class Person:
    def showPerson(self):
        print("I am person from person class")

class Student(Person):
    def showStudent(self):
        super().showPerson()
        print("Student class called")

obj = Student()
obj.showStudent()
#  single inheritance 