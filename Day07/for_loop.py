# For Loop
# A for loop is used to repeat a block of code a fixed number of times.

for i in range(1, 11):
    print(i)

print("Hello")


#print numbers divisible by 5 from 1 to 100
for i in range(5,101,5):      
      print(i)   
      
#print numbers divisible by both 3 and 5 from 1 to 100

for i in range(3,101):
   if (i%3== 0 and i%5== 0) :
    print(i)
    

# create table of any number
a = int(input("enter a number"))
for i in range(1,11):
    print(a * i)
    
    
# create squares from 1 to 10
for i in range(1,11):
 print(i*i)
    
#print cubes from 1 to 10
for i in range(1,11):
 print (i*i*i)  
    
#find sum from 1 to 50
sum = 0
for i in range (1,51):
    sum = sum + i 
print(sum)
    
# find sum of all even number from 1 to 50
sum = 0
for i in range(2,51,2):
    sum = sum + i
print(sum)
    
# count odd numbers from 1 to 100
count = 0
for i in range(1,101,2):
     count = count + 1
print(count)

# print average of 1 to 100
print("print average of 1 to 100")
sum = 0
for i in range(1,101):
    sum = sum + i
average = sum / 100
print (average)

#Find the largest number from 1 to 100.
print("Find the largest number from 1 to 100.")
a = 0
for i in range (1,101):
 if i > a:
    a = i
print(a) 

#Find the smallest number from 1 to 100.
print("#Find the smallest number from 1 to 100.")
a = 100
for i in range(101,0,-1):
    if i < a:
        a = i
print(a)        


for i in range(1,6):
 print(i * "*")