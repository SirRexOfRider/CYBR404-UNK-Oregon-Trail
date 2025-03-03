'''
Author: Anna Gettinger
Project: A Nifty, Dungeons and Dragons-esque, Oregon Trail-esque, Survive the Day at UNK Game™
Purpose: To create a Weapons class to hold weapon data.
Last Edit: 3/2/25
'''

# Create class.
class Weapons:

    # Data attributes.
    __weapon_name = None
    __weapon_damage = None
    __weapon_description = None

    # Init.
    def __init__(self, name=None, damage=None, description=None):
        self.set_weapon_name(name)
        self.set_weapon_damage(damage)
        self.set_weapon_description(description)

    # Helpers.

    # Getters.
    def get_weapon_name(self):
        return self.__weapon_name

    def get_weapon_damage(self):
        return self.__weapon_damage

    def get_weapon_description(self):
        return self.__weapon_description

    # Setters.
    def set_weapon_name(self, weapon_name):
        self.__weapon_name = weapon_name

    def set_weapon_damage(self, weapon_damage):
        self.__weapon_damage = weapon_damage

    def set_weapon_description(self, weapon_description):
        self.__weapon_description = weapon_description

    # To string.
    def __str__(self):
        temp = "Weapon:\n\tName: " + str(self.get_weapon_name()) + "\n\tDamage: " + str(self.get_weapon_damage()) + \
            "\n\tDescription: " + str(self.get_weapon_description()) + "\n"
        return temp
