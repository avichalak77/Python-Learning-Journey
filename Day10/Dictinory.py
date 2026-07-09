#A dictionary is a collection of key-value pairs.

student = {
      "name": "avii",
      "age" : 23,
      "Address": "Pune"
}

student["age"] = {22}     #update data 
student["name"] = {"Avii"}

print(student)

print(student["age"])   #to print only specified item

student["Mobile_no"] = {9999}    #to add new key value pair


student.pop("age")  #pop used to delete a perticular elemet

print(student)

print(student.get("city"))


print(student.keys())     #Returns all the Keys.
print(student.values())  #Returns all the values.
print(student.items())      #Returns both keys and values together.

for key in student:
    print(key)