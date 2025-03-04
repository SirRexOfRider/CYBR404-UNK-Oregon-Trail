class Player:
    
    #DA
    __health = 0
    __equiped_weapon = object
    __location_num = 0
    __inventory = []
    __location_history = []
    
    
    #Init
    def __init__(self, h, ew, ln, i, lh):
        self.set_health(h)
        self.set_equiped_weapon(ew)
        self.set_location_num(ln)
        self.set_inventory(i)
        self.set_location_history(lh)
        
    #Helpers
    def attack(self):
        #Get the weapon object and the weapon damage attribute
        return self.equiped_weapon.get_weapon_damage()
    
    #Display inventory
    def display_inventory(self):
        temp = ["INVENTORY: \n\t"]
        temp_num = 0
        for item in self.get_inventory():
            temp_num += 1
            temp.append(str(temp_num) + ": " + item.get_weapon_name())
            
        return temp
    
    #Change weapon from inventory
    def change_weapon(self, choice = int):
        #Swap currently equiped weapon and one from inventory
        self.get_inventory().append(self.get_equiped_weapon())
        self.set_equiped_weapon(self.get_inventory().pop(choice - 1))
        
    #Add location name to location history list
    def add_location_to_history(self, location):
        self.set_location_history(self.get_location_history().append(location.get_location_name()))
        
            
    #Getters
    def get_health(self):
        return self.__health
    
    def get_equiped_weapon(self):
        return self.__equiped_weapon
    
    def get_location_num(self):
        return self.__location_num
    
    def get_inventory(self):
        return self.__inventory
    
    def get_location_history(self):
        return self.__location_history
    
    #setters
    def set_health(self, h = int):
        self.__health = h
        
    def set_equiped_weapon(self, ew = object):
        self.__equiped_weapon = ew
        
    def set_location_num(self, ln = int):
        self.__location_num = ln
        
    def set_inventory(self, i = []):
        self.__inventory = i
        
    def set_location_history(self, lh = []):
        self.__location_history = lh
        
    
    #To string
    def __str__(self):
        return "PLAYER: \n\tHealth: " + str(self.get_health()) + "\n\tEquiped Weapon: " +  (self.get_equiped_weapon().get_weapon_name()) + "\n\tLocation Number: " + str(self.get_location_num()) \
        + "\n\tInventory: " + str(self.get_inventory()) + "\n\tLocation History: " + str(self.get_location_history())