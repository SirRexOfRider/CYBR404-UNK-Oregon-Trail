#from Enemies import Enemies
from Weapons.Weapons import Weapons
from random import randint



class Events:
        
    #DA
    __weapons_dictionary = {}
    __enemies_dictionary = {}
    __event_running = False


    #------------------------Init-----------------------------------------------------------------------------------------------------------------
    
    #We wouldn't be passing the dictionaries from main, so I guess we make them in the init?
    #The two dictionaries are just made within the set functions
    def __init__(self, running = bool):
        self.set_weapons_dictionary()
        
        #Need enemies file to make this part
        #self.set_enemies_dictionary()
        
        self.set_event_running(running)


    #---------------HELPERS--------------------------------------------------------------------------------------------------------------------
    
    #----------------------MAKE DICTIONARIES-------------------------------------------------------
    def make_weapons_dictionary(self):
        #Access the file and store the file into this temp list
        temp_list = []

        #Open weapons file
        #Might need to include "Project" in front of this file. We can adjust when we start making main
        with open("Code/Weapons/weapons.txt", "r") as file:
            for line in file:
                temp_list.append(line)
            file.close()
                    

        #For objects within the file
        #There's probably a "better way" to do this, but I made it like this because I felt like it.... and also because I don't see an alternative....
        for i in range(0, len(temp_list)):
            
            #Find the indexes of each comma (where different DA's are)
            index = temp_list[i].find(",")
            second_index = temp_list[i].find(",", index + 1)
            
            #Determine which object to create based off what number i is on (what line of the file we're on)
            if i == 0:
                sword = Weapons(temp_list[i][: index], int(temp_list[i][index + 1 : second_index]), temp_list[i][second_index+ 1::])
            elif i == 1:
                calc_book = Weapons(temp_list[i][: index], int(temp_list[i][index + 1 : second_index]), temp_list[i][second_index+ 1::])
            elif i == 2:
                baguette = Weapons(temp_list[i][: index], int(temp_list[i][index + 1 : second_index]), temp_list[i][second_index+ 1::])
            elif i == 3:
                stinky_sneaker= Weapons(temp_list[i][: index], int(temp_list[i][index + 1 : second_index]), temp_list[i][second_index+ 1::])
            elif i == 4:
                gun = Weapons(temp_list[i][: index], int(temp_list[i][index + 1 : second_index]), temp_list[i][second_index+ 1::])
        
        #Put objects into a dictionary
        temp_dictionary = {1:sword, 2:calc_book, 3: baguette, 4:stinky_sneaker, 5: gun}
        
        #Return the dictionary to be set as weapons dictionary
        return temp_dictionary
    
    #Need enemies file for this bit too
    #def make_enemies_dictionary
    
    
    
    #---------------------ROLL D20-------------------------------------------------------------------
    def roll_D20(self):
        return randint(1,20)
    
    #----------------------EVENTS--------------------------------------------------------------------
    
    #Mostly all of these events are going to take in the player object and affect them in some way or another
    #The first one doesn't because it's just going to return the shoes (to initialize player in main)
    
    def begin_journey(self):
        #Concatenate string to print based on what happens
        temp = "\n"
        
        #Story setting!
        temp += "\nYou begin your journey at the... beginning? (duh doi) More specifically, you start your journey at the Arch on the UNK campus.\n"
        temp += "You've been notified that Adam has a new assignment waiting for you in his classroom across campus. You have a ways to walk.\n"
        temp += "Knowing this journey will be long and treachorous, you steal someone else's shoes and use them as psudeo-nunchucks (how or why you did that is not important)\n"
        temp += "You need to choose destinations that will bring you closer to Adam's classroom. The path is up to you...\n"
        temp += "Good luck!\n"
        
        temp += "[Equipeed Stinky Sneakers]\n"
        
        #Print what happened
        print(temp)
        
        #Return weapon to player
        return self.get_weapons_dictionary()[4]
            
        
    def graze(self, player):
        
        #Concatenate string to print based on what happens
        temp = "\n"
        
        temp += "While at the graze: \n"
        
        #SPPIIINN THE WHEEEELLLL
        roll = self.roll_D20()
        
        #Show user what they rolled
        temp += ("\nYou rolled: " + str(roll) + "\n")
        
        #If roll less than or equal to 5
        if roll <= 5:
            temp +="You get dysentary (-50 health)\n"
            player.set_health(player.get_health() - 50)
        
        #If roll greater than or equal to 15  
        elif roll >= 15:
            temp += "You have a very tasty rat tail soup. Yummers? (+30 health)\n"
            player.set_health(player.get_health() + 30)
        
        #Else
        else:
            temp += "You find a baguette lying in a nearby trashcan. It's too stiff to actually eat so you might as well clobber foes with it? [Added Baguette to inventory]\n"
            player.get_inventory().append(self.get_weapons_dictionary()[3])
            
        print(temp)
        return player
            
        
    #Getters
    def get_weapons_dictionary(self):
        return self.__weapons_dictionary

    def get_enemies_dictionary(self):
        return self.__enemies_dictionary

    def get_event_running(self):
        return self.__event_running

    #Setters
    def set_weapons_dictionary(self):
        self.__weapons_dictionary = self.make_weapons_dictionary()
        
    #def set_enemies_dictionary(self):
        #self.__enemies_dictionary = self.make_enemies_dictionary()
    
    def set_event_running(self, bool):
        self.__event_running = bool
        
    #To string
    def __str__(self):
        return "Weapons Dictionary: " + str(self.get_weapons_dictionary())



            





            




