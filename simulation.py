from star import Star
from planet import Planet
from moon import Moon
from utils import plot_orbit

def visualize_orbits(planets):
    for planet in planets:
        plot_orbit(planet.distance_from_star)

def simulate():
    # Create celestial objects
    sun = Star("Sun", 1.989e30, 696340)
    earth = Planet("Earth", 5.972e24, 6371, 149.6e6)
    moon = Moon("Moon", 7.342e22, 1737, 384400)
    
    # Establish relationships
    earth.add_moon(moon)
    
    # Simulation output
    print(sun.shine())
    print(earth.orbit())
    print(moon.orbit())
    print(f"{earth.name} has {len(earth.moons)} moon(s): {[m.name for m in earth.moons]}")
    visualize_orbits([earth]) 