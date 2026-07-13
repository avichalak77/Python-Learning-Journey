try:
    n = int(input("Enter a number:"))
    print(10/n)
except ZeroDivisionError:
    print("Cannot divide by Zero")
    
except ValueError:
    print("Enter a valid Integer")
    
finally:
    print("Program Has ended ")