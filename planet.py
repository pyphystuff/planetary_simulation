############################§
##Define the planet class##
###########################

class Planet:
    def __init__(self, name, mass, radius, distance_from_star, velocity):
        self.name = name
        self.mass = mass
        self.radius = radius 
        self.distance_from_star = distance_from_star
        self.velocity = velocity
        self.moons = []

    def add_moon(self,moon):
        self.moons.append(moon)

    def orbit(self):
        return f"{self.name} is orbiting its star"
