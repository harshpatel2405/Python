class Person:
    def showPerson(self):
        print("Person class called")
    
    
class Student(Person):
    def showStudent(self):
        super().showPerson()
        print("Student class called")
    
    
class TeachingAssitant(Student):
    def showTeachingAssistant(self):
        super().showStudent()
        print("Teaching Assistant class called")
        
obj = TeachingAssitant()
obj.showTeachingAssistant()
# multilevel inheritance