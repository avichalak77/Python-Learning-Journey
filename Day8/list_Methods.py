name = ["Avii","ram","sham","jay"]

#append
print("\nAppend Adds an item at the end.")
name.append("rahul")
print(name)

#insert
print("\nInsert,Adds an item at a specific index.")
name.insert(3,"shree")
print(name)

#remove
print("\nremoves the specific element")
name.remove("shree")
print(name)

#pop
print("\nremove a element by index number")
name.pop(2)
name.pop()         #It removes the last element.
print(name)

#sort
print("\nsorts the numbers")
numbers = [ 85,3,2,56,32,99,4,8]
numbers.sort()
print(numbers)

#reverse
print("\nreverse the list ")
name.reverse()
numbers.reverse()
print(name)

#lenth 
print("\n finds the length of list")
print("lenth of Name_list:",len(name))
print("lenth of Numbers list:",len(numbers))
