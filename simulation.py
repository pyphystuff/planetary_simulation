from star import Star
from planet import Planet
from moon import Moon
from utils import plot_all_orbits
#from utils import rk4

def simulate():
    # Create the star (the Sun)
    #sun = Star("Sun", 1.989e30, 696340, 5778)  # name, mass (kg), radius (km), temperature (K)

    # Create planets with their data
    mercury = Planet("Mercury", 3.3011e23, 2439.7, 57.91e6, 47.870)
    venus   = Planet("Venus",   4.8675e24, 6051.8, 108.2e6, 35.020)
    earth   = Planet("Earth",   5.97237e24, 6371,   149.6e6, 29.780)
    mars    = Planet("Mars",    6.4171e23, 3389.5, 227.9e6, 24.077)
    jupiter = Planet("Jupiter", 1.8982e27, 69911,  778.5e6, 13.070)
    saturn  = Planet("Saturn",  5.6834e26, 58232,  1.433e9,  9.690)
    uranus  = Planet("Uranus",  8.6810e25, 25362,  2.877e9,  6.810)
    neptune = Planet("Neptune", 1.02413e26, 24622, 4.503e9,  5.430)

    # List of all planets
    orbit = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    #orbit = [earth]

    # Simulation output
    #print(sun.shine())
    #for planet in planets:
    #    print(planet.orbit())

    # Visualize orbits
    

    plot_all_orbits(orbit)
