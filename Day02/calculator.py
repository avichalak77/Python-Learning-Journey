a = int(input("Enter First Number :"))
b = int(input("Enter second number :"))

operation = input("Enter Operation (+, -, *, /, % , //): ")
 
if operation == "+":
 answer = a + b 
 print(answer)

elif operation =="-":
    answer = a - b
    print(answer)

    
elif operation == "/":
    if b == 0:
        print("cannot divide by zero")
    else:
     answer = a / b 
    print(answer)
    
elif operation == "*":
    answer = a * b
    print(answer)
    
elif operation =="%":
 answer = a % b
 print (answer)
    
elif operation == "//":
    answer = a // b
    print(answer)


else:
    print("Invalid Operation")