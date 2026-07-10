forts = {"Raigad","Shivneri","Torna","Sinhgad","Lohgad","Raigad","Shivneri"}

print(forts)

forts.add("Rajgad")

# print(forts.remove("Torna"))

forts.remove("Torna")
forts.discard("Pratapgad")

forts.update(["Janjira","Pratapgad","Devgad"])
print(len(forts))