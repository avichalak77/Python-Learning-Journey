#Exception Handling
try:
    n = int(input("Enter a number:"))
    print(10/n)
    
#except runs Only if an exception occurs
except ValueError:             
    print("Enter a valid Interger")

except ZeroDivisionError:
    print("Cannot divide by zero")

#Else runs Only if no exception occurs
else:
    print("No exception occured, Program Successfully executed")
    
#runs Always 
finally:
    print("Program has ended")