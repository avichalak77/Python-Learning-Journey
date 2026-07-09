
# Extract Username from given Email
email = input("Enter your Email:")

username = ""
 
for i in email:
    if i == "@":
        break
    
    username = username + i 
    
print (username,"is Your username")
    