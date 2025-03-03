class Locations:

    __location_name = None
    __location_description = []

    #init
    def __init__(self, location_name, location_description):
        self.set_location_name(location_name)
        self.set_location_description(location_description)

    #getters
    def get_location_name(self):
        return self.__location_name

    def get_location_description(self):
        return self.__location_description

    #setters
    def set_location_name(self, location_name):
        self.__location_name = location_name

    def set_location_description(self, location_description):
        self.__location_description = location_description

    #tostring
    def __str__(self):
        return "You are at " + str(self.get_location_name()) + str(self.get_location_description())
