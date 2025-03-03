#from Enemies import Enemies
from Weapons import Weapons


#This is just for testing. This is how I was able to read the file
temp_list = []
with open("Project/Code/Weapons/weapons.txt", "r") as file:
    for line in file:
        temp_list.append(line)
        
print(temp_list[0])

w1 = Weapons("Knife", 10, "Pointy")

