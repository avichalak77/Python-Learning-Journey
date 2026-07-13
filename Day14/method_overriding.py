class Animal:
    def sound(self):
        print("Animal Makes Sound")
        
class Dog(Animal):
    def sound(self):
        super().sound()  #Calls the parent class method or constructor
        print("Dog Barks")
        
d1 =Dog()
d1.sound()





class Employee:
    def work(self):
        print("Employee is Working")
        
class Manager(Employee):
    def work(self):
        print("Manager is managing the team")
        
m1 = Manager()
m1.work()