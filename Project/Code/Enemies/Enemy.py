class enemy:
    _atk = 30
    _hp = 100
    _name = "Chaddragon"
    _description = "You have found the dastardly beast that has kidnapped your Professor!\n Its Sigma shiny scales cover it’s large CHAD body to give it 100 HP.\n Its claws are made of rizz to give it an ATK power of 30.\n\n Defeat the beast known as the Chaddragon to save your Professor!"

    def __init__(self, name, attack, hp, description):
        self._name = name
        self._atk = attack
        self._hp = hp
        self._description = description

    def get_atk(self):
        return self._atk

    def get_hp(self):
        return self._hp

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description

    def set_atk(self, atk):
        self._atk = atk

    def set_hp(self, hp):
        self._hp = hp
