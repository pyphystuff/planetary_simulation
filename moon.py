class Moon:
    def __init__(self, name, mass, radius, distance_from_planet):
        self.name = name
        self.mass = mass
        self.radius = radius
        self.distance_from_planet = distance_from_planet


    def orbit(self):
        return f"{self.name} is orbiting planet"    