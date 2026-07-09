def greet():
    print("Welcome in the world of python")
    print("This is a function")
greet()


def add():
    a = 10
    b = 20
    print(a + b)
    
add()


def square():
    a = 5
    print(a*a)
square()


def numbers():
    for i in range(1,6):
        print(i)
numbers()


def table():
    for i in range(1,11):
        print("5 x",i,"=" ,5 *i)
table()        
    
def name():
    a = "Avii"
    b = 10
    print(a*b)    
name()        
# or
def name():
    n = "avii"
    print( n * 10)
name()    

    
def table(number):
    for i in range(1,11):
      print(number,"x",i,"=",i*number)
table(8)   
        