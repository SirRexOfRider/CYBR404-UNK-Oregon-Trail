[Home Page](https://github.com/SirRexOfRider/CYBR404-UNK-Oregon-Trail/tree/main)
<hr>

**Problem summary:** 

A Nifty Dungeons and Dragons-esque, Oregon Trail-esque, Survive the day at UNK Game TM, the game will operate on main.py or python and uses a command line interface for the user to enter input.

To start we are given Enemy Files and it is required to have statistics relating to the enemies health and attack, Enemy files also requires events to be stored so they can be utilized at given locations, this would basically mean assigning an enemy to a location for the player to come across, and the Enemy file is required to determine if a player won or  lost based on health, if the enemy is left with zero health the enemy has lost (for this assignment, the only enemy type will be the dragon at the end due to the time crunch. Having this file is more of a "what/how we would implement" if we had the time).


The next given is Weapons file, it is required to store statistics/descriptions for weapons such as swords or dagger and the amount of damage they deal. It is also required that weapons are able to be used during an event, lastly for weapons files it is required that there is an inventory to store the weapons in so there is a way to keep track of them.


The next given is the Events file, which requires there be some chance of a random event happening between locations it also requires that events can be stored and used at locations, this means an event can be planned and not just random.


Another given is the Location file, which requires that there must be some chance of random events happening between locations, it requires that stored events can be used at locations, it is also required to store location/route description so the player has a sense of where they are in the game and lastly it is required to determine if the player won or lost based off location and health.


The following given is the Player Character File which requires player health to be stored, this is an important requirement as the player needs health in a game with fighting. Another requirement is to determine if the player won or lost if the player makes it all the way through with health left they won, the final requirement for this one is it needs to store/change the players location so this would be used when a player selects the next location.


Lastly is the machine that runs the game which like I said at the start is main.py and does have a good amount of requirements, to start it is required to use a D20 to get a random number and determine a success or failure, the next requirement is very important and that is validating user input, this is essential for the game to run correctly or at all. It is required that a player is able to quit the game if they would like to so like an exit button, it is also required that a list of all available options must be presented to player per turn like selecting weapon or choose the next location after a event. Another requirement is the player must be able to interact with events/locations and the player must have multiple options to interact with like run, attack or inspect, it is required that events with an enemy the enemy or player health must reach zero for the event to end, it also is required to determine if a player has won or lost and again that’s based on health and location, Lastly it is required to store/change a players location. 
