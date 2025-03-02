[Home]()

4.1 Executive Design Statement

4.1.1 Components

Our project will utilize a double while loop structure that tracks whether the game is running, as well as whether the player is still alive. 

The game will have several classes representing different objects in our game: Player, Weapons, Enemies, Events, and Locations. Additionally, the main.py of our program will have several variables and helper functions of its own to complete the program. Specifically:

•	main.py
o	Data attributes: 
	Name: locations_dictionary
•	Type: dictionary 
•	Description: holds all locations and descriptions as key-value pair
	Name: game_running
•	Type: Boolean
•	Description: tracks whether game is still running
	Name: player_alive
•	Type: Boolean
•	Description: tracks whether player is still alive or not 
	Name: current_location
•	Type: str
•	Description: tracks where player currently is in the game 
o	Helpers: 
	Name: calculate_next_location()
•	Description: gets information to display to user next available locations based on current location 
	Name: game_over()
•	Description: gives player information about what happens once the game is over and how to start a replay, if desired 

4.1.2 Entities 

We will have only one entity in our project. Namely, the sole entity in our project will be the player(s) of our game. 

4.1.3 Processes and Data Flows 

Our project has many interconnected processes (P) and data flows (DF). In our project, the user entity starts the game (DF) and prompts the game initializer (P). Input from the user is validated (DF) through the input validator (P), with the input being compared (DF) to the allowable data in the data store input data. The input data store then returns (DF), connecting all inputted data and the input validator (P) back to the game initializer (P). 

From the game initializer (P), input data is sent to (DF) the game controller (P). The game controller (P) sends the player choice (DF) to get player choice data (P), which then needs to be validated (DF) by input validation (P). 

The input validation (P) compares (DF) inputted data against allowable data in the input data store, with the result retrieved (DF) back to input validation (P). From input validation (P), data flows lead to location choice (P), action/weapon choice (P), and random D20 event data (P). 

Location choice (P) is connected to the data store location data by data flows get and return. The processes location choice and action/weapon choice connect back to game controller (P) by separate data flows, both called selects choice.

The random D20 event data process connects to roll D20 (P) by tells dice to roll (DF) and return roll (DF), as well as event data (P) by determines random event (DF). The event data process connects to two data stores: weapon data by data flows get and returns, and enemy data by data flows get and returns. The process event data also loops back (DF) to process game controller.

4.1.4 Data Stores

We will have several data stores in our project. Specifically, we will have: an inventory list, an a weapons dictionary, enemies dictionary, a locations dictionary, a location history list, an input data list, weapons .txt file, enemies .txt file, and a locations .txt file. 

The inventory list will store weapon objects that the user picks up in gameplay for use in the final battle. Additionally, the enemies dictionary will store information about enemy objects, the weapons dictionary will store information about the individual weapons objects, and the locations dictionary will store information about the individual location objects. Furthermore, the location history list will keep track of which locations the user has visited. Finally, the input data list holds a list of all allowable user input for user input to be compared against and either rejected or accepted. The weapons, enemies, and locations .txt files will hold the information that will loaded into the weapons, enemies, and locations dictionaries.

The data stores will be formatted as follows:

•	Name: inventory
•	Type: list
•	Description: tracks what the player has collected in their inventory
•	Name: weapons_dictionary
•	Type: dictionary
•	Description: dictionary holding all weapons
•	Name: enemies_dictionary
•	Type: dictionary 
•	Description: dictionary holding all enemies
•	Name: locations_dictionary
•	Type: dictionary
•	Description: dictionary holding all location data 
•	Name: location_history
•	Type: list
•	Description: keeps track of where the player has been
•	Name: input_data
•	Type: list
•	Description: holds all allowable user inputs to compare user input against 
•	Name: weapons.txt
•	Type: .txt file
•	Description: holds data to be loaded into weapons dictionary 
•	Name: enemies.txt
•	Type: .txt file
•	Description: holds data to be loaded into enemies dictionary 
•	Name: locations.txt
•	Type: .txt file
•	Description: holds data to be loaded into locations dictionary 

4.1.5 Classes

Classes will be made for the Player, Weapons, Enemies, Events, and Locations. All the classes, their data attributes, and any helper functions are outlined below: 

•	Player 
	Data attributes:
•	Name: health
o	Type: int
o	Description: tracks player’s health to know if the player is dead or not
•	Name: equipped_weapon
o	Type: object 
o	Description: tracks what weapon the user has equipped
•	Name: location_num
o	Type: int
o	Description: tracks how many locations the player has visited 
•	Name: inventory
o	Type: list
o	Description: tracks what the player has collected in their inventory
•	Name: location_history
o	Type: list
o	Description: keeps track of where the player has been
	Helpers:
•	Name: attack()
o	Returns an int for damage
•	Name: display_inventory()
o	Returns list showing the player’s inventory
•	Name: change_weapon()
o	Allows the user to change out their weapon and swap items in and out of inventory
•	Name: add_location_to_history()
o	Adds a location that’s been visited to the location history list 
•	Locations
	Data attributes:
•	Name: location_name
o	Type: int
o	Description: assigns number to location
•	Name: location_description
o	Type: str
o	Description: gives a description to the user of the location where they’re currently at
•	Events
	Data attributes:
•	Name: weapons_dictionary
o	Type: dictionary
o	Description: dictionary holding all weapons, with keys being selection from keyboard (i.e., “1 for sword, 2 for baguette”, etc.)
•	Name: enemies_dictionary
o	Type: dictionary 
o	Description: dictionary holding all enemies
•	Name: event_running
o	Type: Boolean
o	Description: check if event is running or not 
	Helpers:
•	Name: roll_D20()
o	Returns int using Random module for use in random choice generation for events 
•	Methods for events at set locations
o	Takes in player
•	Methods for random events
o	Takes in player 
•	Enemies 
	Data attributes:
•	Name (str)
•	Health (int)
•	Damage (int)
•	Description (str)
•	Weapons 
	Data attributes:
•	weapon_name (str)
•	weapon_damage (int)
•	weapon_description (str)

4.1.6 Objects

There will be one object created of the Player class to represent the user, with the Player being recreated if the player dies and starts the game over.

There will be one object created of the Enemies class to create the Loper dragon boss at the end of the game. If the game is expanded, we hope to add more enemies that the player could encounter on their journey beyond environmental hardships. 

There will be five different objects of the Weapon class created to represent the five different weapons that the user can pick up during the game. These objects will be: sword, Calculus textbook, baguette, stinky sneaker, and gun.

There will be four objects created from the Locations class each gameplay. The last object will always be Discovery Hall Room 206, as this is the location of the final boss battle. However, the other locations may change depending on where the user decides to go. The user will be able to choose between the following potential locations: the Union, the Graze, the Health and Sports Center, the Fine Arts Building, the Memorial Student Affairs Building, Warner Hall, and Discovery Hall. 

The Event class will run depending on whether or not an event is running. Instances of the Event class will be created accordingly as needed.

4.1.7 Data Formats

Our project will utilize several different data formats, namely string, integer, and .txt files. 

4.1.8 User interactions

The user will be able to interact with the program on Python IDE PyCharm’s command line after the program has started to run. Menu choices will be given to the user so that they can navigate the game, with instructions displayed to help the user understand what each choice will entail. 

The menu will give the user the following global choices:

•	View Inventory
•	View Instructions 
•	Quit Game 

There will also be another menu shown to the user to allow them to choose their location, with only close by locations shown as options they can choose as they progress.


[Back to Design](https://github.com/SirRexOfRider/CYBR404-UNK-Oregon-Trail/blob/main/Project/Design/Design.md)
