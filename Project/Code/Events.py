from Enemies.Enemy import enemy
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
        self.set_enemies_dictionary()
        self.set_event_running(running)



    #---------------HELPERS--------------------------------------------------------------------------------------------------------------------
    
    #----------------------MAKE DICTIONARIES-------------------------------------------------------
    def make_weapons_dictionary(self):
        #Access the file and store the file into this temp list
        temp_list = []

        #Open weapons file
        #Might need to include "Project" in front of this file. We can adjust when we start making main
        with open("Project/Code/Weapons/weapons.txt", "r") as file:
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
    
    def make_enemies_dictionary(self):
        #Access the file and store the file into this temp list
        temp_list = []

        #Open enemy file
        #Might need to include "Project" in front of this file. We can adjust when we start making main
        with open("Project/Code/Enemies/Enemy.txt", "r") as file:
            for line in file:
                temp_list.append(line)
            file.close()
                    

        #For objects within the file
        #There's probably a "better way" to do this, but I made it like this because I felt like it.... and also because I don't see an alternative....
        for i in range(0, len(temp_list)):
            
            #Find the indexes of each comma (where different DA's are)
            index = temp_list[i].find(",")
            second_index = temp_list[i].find(",", index + 1)
            third_index = temp_list[i].find(",", second_index + 1)
            
            #Determine which object to create based off what number i is on (what line of the file we're on)
            if i == 0:
                dragon = enemy(int(temp_list[i][: index]), int(temp_list[i][index+1 :second_index]), temp_list[i][second_index + 1 : third_index], temp_list[i][third_index + 1::])
        
        #Put objects into a dictionary
        temp_dictionary = {1 : dragon}
        
        #Return the dictionary to be set as weapons dictionary
        return temp_dictionary
    
    
    
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
    
    def union(self, player):
        #Concatenate string to print based on what happens
        temp = "\n"
        
        temp += "While at the union: \n"
        
        #SPPIIINN THE WHEEEELLLL
        roll = self.roll_D20()
        
        #Show user what they rolled
        temp += ("\nYou rolled: " + str(roll) + "\n")
        
        #If roll less than or equal to 5
        if roll <= 5:
            temp +="You get trampled by the line (-10 health)\n"
            player.set_health(player.get_health() - 10)
        
        #If roll greater than or equal to 15  
        elif roll >= 15:
            temp += "You apply your *five finger discount* and steal someone else's lunch. You monster..... (+20 health)\n"
            player.set_health(player.get_health() + 20)
        
        #Else
        else:
            temp += "You successfully avoid the line and the journey continues!\n"

            
        print(temp)
        return player
    
    def hasc(self, player):
        #Concatenate string to print based on what happens
        temp = "\n"
        
        temp += "While at the Health and Sports Center: \n"
        
        #SPPIIINN THE WHEEEELLLL
        roll = self.roll_D20()
        
        #Show user what they rolled
        temp += ("\nYou rolled: " + str(roll) + "\n")
        
        #If roll less than or equal to 5
        if roll <= 5:
            temp +="You get hit by a flying dumbell. Pain is gain? (-30 health)\n"
            player.set_health(player.get_health() - 30)
        
        #If roll greater than or equal to 15  
        elif roll >= 15:
            temp += "A gym bro gives you a reassuring thumbs up. It heals your soul! (+30 health)\n"
            player.set_health(player.get_health() + 30)
        
        #Else
        else:
            temp += "You sucessfully dodge all of the flying dumbells and get assisted by a jock who launches you straight into Adam's room (don't ask about logistics, just roll with it...)\n"
            
        print(temp)
        return player
    
    def msab(self, player):
        #Concatenate string to print based on what happens
        temp = "\n"
        
        temp += "While at the Memorial Student Affairs Building: \n"
        
        #SPPIIINN THE WHEEEELLLL
        roll = self.roll_D20()
        
        #Show user what they rolled
        temp += ("\nYou rolled: " + str(roll) + "\n")
        
        #If roll less than or equal to 5
        if roll <= 5:
            temp +="You get crushed by a mountain of paperwork. After walking out of it, you have so many paper cuts that it looks like a gang cats just mugged you! (-20 health) \n"
            player.set_health(player.get_health() - 20)
        
        #If roll greater than or equal to 15  
        elif roll >= 15:
            temp += "You spot a sword laying amongst the piles of paperwork. Surely no one will be needing this.... [Added Sword to Inventory]\n"
            player.get_inventory().append(self.get_weapons_dictionary()[1])
        
        #Else
        else:
            temp += "FASFA's can wait....(right?) You continue on!\n"
            
        print(temp)
        return player
    
    def discovery_hall(self, player):
        #Concatenate string to print based on what happens
        temp = "\n"
        
        temp += "You make it to discovery hall. You're so close adam's class! \n"
        
        #SPPIIINN THE WHEEEELLLL
        roll = self.roll_D20()
        
        #Show user what they rolled
        temp += ("\nYou rolled: " + str(roll) + "\n")
        
        #If roll less than or equal to 5
        if roll <= 5:
            temp +="A student throws their Calculus book flying across the hall in a fit of rage (hey I don't blame you). You notice this becuase about a second later, said textbook hits you straight in the face. Ow! [-20 health]\n"
            player.set_health(player.get_health() - 20)
        
        #If roll greater than or equal to 15  
        elif roll >= 15:
            temp += "You find a very heavy calculus textbook lying on the ground (probably thrown out of rage) and decide to use it as a weapon [Added Calculus Textbook to Inventory]\n"
            player.get_inventory().append(self.get_weapons_dictionary()[2])
        
        #Else
        else:
            temp += "You walk up the stairs and approach Adam's classroom\n"
            
    def warner_hall(self, player):
        #Concatenate string to print based on what happens
        temp = "\n"
        
        temp += "You make it to discovery hall. You're so close adam's class! \n"
        
        #SPPIIINN THE WHEEEELLLL
        roll = self.roll_D20()
        
        #Show user what they rolled
        temp += ("\nYou rolled: " + str(roll) + "\n")
        
        #If roll less than or equal to 5
        if roll <= 5:
            temp +="A student throws their Calculus book flying across the hall in a fit of rage (hey I don't blame you). You notice this becuase about a second later, said textbook hits you straight in the face. Ow! [-20 health]\n"
            player.set_health(player.get_health() - 20)
        
        #If roll is a 20 
        elif roll == 20:
            temp += "You find a gun.... I... who would even... you know what? Have it! I didn't care about balancing anyways... [Added Gun to Inventory]\n"
            player.get_inventory().append(self.get_weapons_dictionary()[5])
        
        #Else
        else:
            temp += "The building is uneventful as it is dusty. You decide to move on!"
            
        
        print(temp)
        return player
    
    
    #DRAGON FIGHT
    def dragon_fight(self, player):
        
        #Make string to concatenate
        temp = "\n"
        
        temp += "A dragon has captured adam and is holding him hostage! You're the only one that can save him. You approach the dragon ready to slay it! \n"
        
        #Not quite sure if this bit will work but we'll try it
        temp += self.get_enemies_dictionary()[1]
        
        temp+= "\n~~~~~~~~~~~~~~~~~~~~~~~~~~COMBAT LOG~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        
        
        #This event is gonna be a little different. It's basically going to go until either dragon health hits zero or player does.
        #Random D20 will still determine if either hit each other with attacks
        
        while (self.get_event_running()):
            
            #SPPIIINN THE WHEEEELLLL
            roll = self.roll_D20()
            
            #Player attack
            temp += "PLAYER ATTACK: ----------------------------------------------"
            
            if roll >= 10:
                temp += "\n You attack the dragon and it does damage!"
                self.get_enemies_dictionary()[1].set_hp(self.get_enemies_dictionary()[1].get_hp() - player.attack())
            else:
                temp += "\nYour attack misses!"
            
            temp += "------------------------------------------------------------"
            
            temp += "DRAGON ATTACK: #############################################"
            if roll >= 10:
                temp += "\n The dragon attack the you and it does damage!"
                player.set_health(player.get_health() - self.get_enemies_dictionary()[1].get_atk())
            else:
                temp += "\nThe Dragon's attack misses!"
            
            temp += "############################################################"
            
            #Check if either player or dragon is dead
            if player.get_health() <= 0 or self.get_enemies_dictionary()[1].get_hp() <= 0:
                self.set_event_running(False)
            
        
        temp+= "\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        
        #Return player after event is done (either dead or alive)
        return player
            
    #--------------GETTERS----------------------------------------------------------------------------------------------------------------------
    def get_weapons_dictionary(self):
        return self.__weapons_dictionary

    def get_enemies_dictionary(self):
        return self.__enemies_dictionary

    def get_event_running(self):
        return self.__event_running

    #------------SETTERS--------------------------------------------------------------------------------------------------------------------------
    def set_weapons_dictionary(self):
        self.__weapons_dictionary = self.make_weapons_dictionary()
        
    def set_enemies_dictionary(self):
        self.__enemies_dictionary = self.make_enemies_dictionary()
    
    def set_event_running(self, bool):
        self.__event_running = bool
        
    #----------TO STRING-------------------------------------------------------------------------------------------------------------------------
    def __str__(self):
        return "EVENTS: \n\tWeapons Dictionary: " + str(self.get_weapons_dictionary()) +"\n\tEnemies Dictionary: " + str(self.get_enemies_dictionary()) + "\n\tIs Event Running?: " + str(self.get_event_running())



            





            




