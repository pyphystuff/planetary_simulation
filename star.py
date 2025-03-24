##########################
##Define the star class##
#########################
class Star:
    def __init__(self, name, mass, radius):
        self.name = name
        self.mass = mass
        self.radius = radius

    def shine(self):
        return f"{self.name} is shining brightly!"
