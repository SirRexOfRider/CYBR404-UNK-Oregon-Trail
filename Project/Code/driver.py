from Locations.Locations import Locations
from Player import Player
from Events import Events

__locations_dictionary = {}
events = Events(True)



def main():
    
    # Call functions to read in file data, create objects, and print out new objects.
    __locations_dictionary = read_file("Project/Code/Locations/Locations.txt", Locations)
    running = True
    player_alive = True
    __accepted_inputs_main = [1,2,3,4]
    __accepted_inputs_events = [1, 2]
    
    
    
    
    while running:
        temp = ""
        temp += "-----------------------------------------------------------------------------------------\n"
        temp += "- A Nifty, Dungeons and Dragons-esque, Oregon Trail-esque, Survive the Day at UNK Game™ -\n"
        temp += "-----------------------------------------------------------------------------------------\n"
        temp += ("\nYou are at:")
        temp += str(__locations_dictionary[0])
        print(temp)
        
        player = Player(100, events.begin_journey(), 0, [], [])
        
        
        
        while player_alive:
            
            temp = ""
            temp +="~~~~~~ OPTIONS ~~~~~~~~~\n"
            temp +="1. Display Inventory\n"
            temp +="2. Change Weapon\n"
            temp +="3. Display Player data\n"
            temp +="4. Change location\n"
            temp +=("~~~~~~~~~~~~~~~~~~~~~~~~~\n")
            print(temp)
            
            #Validate user input
            try:
                ui = int(input("Please enter option of cooresponding number: "))
                print("\n")
                
                #Compare to expected whitelisted values
                if ui in __accepted_inputs_main:
                    
                    #If user chooses 1
                    if ui == 1:
                        #Print player inventory
                        print(player.display_inventory())
                        print()
                        
                    #If user chooses 2
                    elif ui == 2:
                        
                        #If user has nothing in their inventory
                        if len(player.get_inventory()) == 0:
                            print("You have no weapons to currently swap to!")
                            print()
                            continue
                        
                        #If user has something in their inventory, display options and let them swap
                        print()
                        print(player.display_inventory())
                        print()
                        
                        #Try
                        try:
                            
                            ui2 = int(input("Which weapon would you like to swap to?: "))
                             #IF user input is between 1 and length of the inventory
                            if ui2 <= len(player.get_inventory()) and ui2 >= 1:
                                #Change weapon
                                player.change_weapon(ui2)
                        
                            #Kick user back to try again
                            else:
                                print("Error, please try again!")
                                continue
                        
                        #Except anything else. While loop continues
                        except Exception as e:
                            print(e)
                        
                       
                    
                    #if user chooses 3
                    elif ui == 3:
                        #Print player data
                        print(player)
                        print("\n")
                        
                    #if user chooses 4
                    elif ui == 4:
                        
                        #Calculate availabe stops from current location
                        available_locations = calc_locations(player.get_location_num())
                        print("Available Locations: \n")
                        print(str(available_locations[0]) + ": " + str(__locations_dictionary[available_locations[0]].get_location_name()))
                        print(str(available_locations[1]) + ": " + str(__locations_dictionary[available_locations[1]].get_location_name()))
                        print()
                        
                        
                        try:
                            #Get user input
                            ui3 = int(input("Please choose your next stop!: "))
                            print("\n\n")
                            
                            #If input is an available location
                            if ui3 in available_locations:
                                
                                #Add location to history list
                                player.get_location_history().append(__locations_dictionary[ui3].get_location_name())
                                #Change current location number
                                player.set_location_num(ui3)
                                
                                #Print location data
                                print(__locations_dictionary[ui3])
                                
                                #Calculate event that happens at that location. Bring in player so events can change it
                                calc_event(ui3, player)
                                calc_game_over(player)
                                
                            
                            #ERRORRRRRRR
                            else:
                                print("Error, not an avaialbe location!")
                                continue
                        
                        #Except anything else. While loop continues
                        except Exception as e:
                            print(e)
                                
                        
                    
                        
                            
                #If user input is not in accepted inputs [1-4]
                else:
                    print("Please enter number [1-4]")
                    continue
                

                
                
            #Catch bad input (naughty naughty!!!)    
            except Exception as e:
                print(e)
        
        #This is for when player dies / finishes game
        ui4 = input("Would you like to play again? [Enter / heck yes!] [Anything else / heck no!]: ")
        
        #If input is not enter
        if ui4 != "":
            
            #End program
            running = False    
        
#Calculate locations based off current location number  
def calc_locations(num):
    
    accepted_input_events = [0,0]
    
    if num == 0:
        accepted_input_events = [1,2]
    elif num == 1 or num == 2:
        accepted_input_events = [3, 4]
    elif num == 3 or num == 4:
        accepted_input_events = [5,6]
    elif num == 5 or num == 6:
        accepted_input_events = [7, 7]
        
    return accepted_input_events

#Calculte events based off current location number
def calc_event(num, player):
    if num == 1:
        events.warner_hall(player)
    elif num == 2:
        events.graze(player)
    elif num == 3:
        events.msab(player)
    elif num == 4:
        events.union(player)
    elif num == 5:
        events.hasc(player)
    elif num == 6:
        events.discovery_hall(player)
    elif num == 7:
        events.dragon_fight(player)

#Calculate if the game is over depending on player health and location
#Return if game is still running after this check as well
def calc_game_over(player):
    
    #String to concatenate
    temp = ""
    player_alive = True
    
    #If player dies before getting to the dragon fight
    if player.get_health() <= 0 and player.get_location() != 7:
        temp += "+---------------------------+\n"
        temp += "|      G A M E  O V E R     |\n"
        temp += "+---------------------------+\n"
        
        temp += "You perish on the way to adam's classroom. How are you going to get your degree now?!?\n"
        player_alive = False
        
    #If player dies at dragon fight
    if player.get_health() <= 0 and player.get_location() == 7:
        temp += "+---------------------------+\n"
        temp += "|      G A M E  O V E R     |\n"
        temp += "+---------------------------+\n"
        
        temp += "You were eeviscerated by the dragon! It's mog-maxxing was too much!!!\n"
        player_alvie = False
        
    #If player wins!!!
    if player.get_health() <= 0 and player.get_location() == 7:
        temp += "+---------------------------+\n"
        temp += "|      Y O U  W I N ! !     |\n"
        temp += "+---------------------------+\n"
        
        temp += "You absolutely demolished that dragon! Adam is very pleased with you and will probably give you extra credit.... right?...\n"
        temp += ("PLAYER STATS: \n" + player)
        
        #Technically no, the player doesn't die but this breaks the loop for the main game
        #"I've won, but at what cost? haha"
        player_alive = False
        
        print(temp)
        
    return player_alive
        
        
        
        
        
    
        
        
    
        
    
    

# Create function to read in data from file to create objects.
def read_file(file, class_name):
    object_list = []
    temp_dictionary = {}
    with open(file, "r") as f:
        for line in f:
            c1 = class_name(line.split(",")[0].strip(), line.split(",")[1].strip())
            object_list.append(c1)
            
        for i in range(0, len(object_list)):
            temp_dictionary[i] = object_list[i]
    return temp_dictionary

# Create function to print out objects from object list.
def print_objects(ld):
    for object in ld:
        print(object)


    
    
        

        
    

if __name__ == '__main__':
    main()
