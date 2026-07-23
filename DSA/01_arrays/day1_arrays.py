# An Array is a collection of elements stored in continuous memory locations.
# In Python, we generally use lists to implement arrays.

a = [ 12,22,14,53,75,82]

#Accessing Elements
print(a[0])
print(a[4])
print(a[:3])

#Updating Elements
a[1]=25
a[0]=9
print(a)

#traversing an array
for i in a:
    print(i)


print(len(a))
print(a[5])

for i in a:
    if i > 50:
       print(i,">50")

print(sum(a))
print(sum(a)/len(a))


for i in a:
  if i % 2 == 0:
   print(i," is Even")
   print(a.count)
  else:
     print(i,"is odd")

print(a)


p = 0
for i in a:
   if i> p:
      p = p + i
      print(i)