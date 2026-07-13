class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
       print("Hello",self.name)
    
s1 = student("Govind",23)
s2 = student("Shubham",24)

s2.greet()
s1.greet()





class Bankaccount:
    def __init__(self, account_holder, balance):
       self.account_holder = account_holder
       self.balance = balance
       
    def show_balance(self):
           print(self.account_holder, self.balance)
           
b1 = Bankaccount("Ram",70000)  
b2 = Bankaccount("DP", 80000)        

b1.show_balance()
b2.show_balance()
           
    