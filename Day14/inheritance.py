class Animal:
    def __init__(self,name):
        self.name = name 
    def name_of(self):
        print("animal is", self.name)
        
a1 = Animal("Goat")

class Dog(Animal):
    pass
a2 = Dog("Cow")

a2.name_of()
a1.name_of()
 
 
 
class Person():
    def __init__(self,name):
        self.name = name
    
    def introduce(self):
        print("My name is", self.name)
        
class Student(Person):
    def __init__(self,name,branch):
        super().__init__(name)
        self.branch = branch
        
    def show_branch(self):
        print("Branch:", self.branch)

s1 = Student("Avii", "AIML")

s1.introduce()
s1.show_branch()