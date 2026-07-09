marks = int(input("Enter Your Marks:"))

if marks < 0 or marks > 100:
    print("Invalid Marks")
    
elif marks >= 90:
    print("you got A+ Grade")
    
elif marks >= 80:
    print("You got A grade")  
    
elif marks >= 70:
    print("You Got B+ grade")

elif marks >= 60:
    print ("You Got B Grade")
    
elif marks >= 50:
    print("You got C grade")
    
elif marks >= 40:
    print("You got D Grade")

else:
    print("You Failed in Exam")    