def greet():
    message = "Hello"
    print(message)
       
# Here, message is a local variable.
# It cannot be accessed outside the function.

# global variable
name = "Avii"    #Here, name is a global variable.

def greet():
    print(name)
greet()



x = 10

def fun():
    y = x + 5
    print(y)

fun()