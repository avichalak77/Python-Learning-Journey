def table(number):
    for i in range(1,11):
      print(number,"x",i,"=",i*number)
table(8)   
        
        
def add(a,b):
    print(a+b)
add(10,20)            
        
        
def square_of_numbers(n):
     print(n*n)
square_of_numbers(7)     
           

def greet(name):
    print("hello",name)
greet("Aviiii")    
           
           
def largest(a,b):
    if a > b:
        print(a)
    else:
        print(b)            
largest(100,1)    


def even_odd(a):
    if a%2 == 0:
        print("Number is Even")
    else:
        print("number is odd")
even_odd(7)        


def factorial(n):
    fact = 1
    for i in range(1,n+1):
     fact = fact * i
    print(fact)
factorial(4)     


def greet(name):
    print(f"Hello {name}")
    
greet("Avii")    


def mul(a,b):
    return a * b
print(mul(4,6))

def add(a,b):
    return a + b 
print(add(1,4))


def substract(a,b):
    return a - b
x= substract(8,4)
print(x)


def add (a,b):
    print(a + b)
    # return a + b
x = add(4,5)


def test(a):
    a = a + 5
    return a

x = 10

print(test(x))
print(x)
