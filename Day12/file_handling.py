file = open("Day12/student.txt", "r")
print(file.read())
file.close()
  


with open("Day12/notes.txt","w") as file:  #write into files
    file.write("Python is awesome")

with open("Day12/notes.txt","a") as file:      # append into files 
    file.write("\n I love Coding")
    
with open("Day12/notes.txt","r") as file:
    for line in file:     #⭐ Reading Line by Line
        print(line)
        
with open("Day12/notes.txt", "r") as file:
    lines = file.readlines()     #Reads all lines into a list.

print(lines)


with open("Day12/notes.txt", "r") as file:
    print(file.readline())     #Reads one line at a time.
    
    
with open("Day12/student.txt","a")as file:
    file.write("\n Name:DP\n Age:21\nBranch:CS")
