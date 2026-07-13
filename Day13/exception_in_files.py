try:
    with open("Day12/note.txt","r") as file:
        print(file.read())
        
except FileNotFoundError:
    print("File Not Found")
        