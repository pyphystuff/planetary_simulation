from star import Star
from planet import Planet
from moon import Moon
from utils import plot_all_orbits



def simulate():
    # Create the star (the Sun)
    #sun = Star("Sun", 1.989e30, 696340, 5778)  # name, mass (kg), radius (km), temperature (K)

    # Create planets with their data
    mercury = Planet("Mercury", 3.3011e23, 2439.7, 57.91e6)  # name, mass (kg), radius (km), distance from Sun (km), orbital speed (km/s)
    venus = Planet("Venus", 4.8675e24, 6051.8, 108.2e6)
    earth = Planet("Earth", 5.97237e24, 6371, 149.6e6)
    mars = Planet("Mars", 6.4171e23, 3389.5, 227.9e6)
    jupiter = Planet("Jupiter", 1.8982e27, 69911, 778.33e6)
    saturn = Planet("Saturn", 5.6834e26, 58232, 1429.4e6)
    uranus = Planet("Uranus", 8.6810e25, 25362, 2870.99e6)
    neptune = Planet("Neptune", 1.02413e26, 24622, 4498.3e6)

    # List of all planets
    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]

    # Simulation output
    #print(sun.shine())
    for planet in planets:
        print(planet.orbit())

    # Visualize orbits
 
    plot_all_orbits(planets)
