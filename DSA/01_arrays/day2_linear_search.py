numbers = [10,20,30,40,50]

target = 10

found = False

for i in numbers:
    if i == target:
      found = True
    break

if found:
   print("Element found")
else:
   print("Not found")


number = [10,20,30,10,10,40,10,50]
count = 0
for i in number:
   if i == 10:
    # count = count + 1
    count += 1
print(count)
   
