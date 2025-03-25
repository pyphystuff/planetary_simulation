import math
import matplotlib.pyplot as plt


def calculate_gravitational_force(m1, m2, distance):
    G = 6.67430e-11  # Gravitational constant
    if distance == 0:
        return 0
    return G * (m1 * m2) / (distance**2) 

##updating positions
###esto hay q pasarlo a las leyes de kepler
def update_position(distance, speed, time):
    angle = (speed*time)%(2*math.pi)
    x = distance*math.cos(angle)
    y = distance*math.sin(angle)
    return x,y

def plot_all_orbits(planets):
    # Plot orbits for each planet
    for planet in planets:
        theta = [i * 0.01 for i in range(0, 628)]  # Generate angles from 0 to 2π
        x = [planet.distance_from_star * math.cos(t) for t in theta]
        y = [planet.distance_from_star * math.sin(t) for t in theta]
        plt.plot(x, y, label=planet.name)  # Label for each planet

    # Customize the plot
    plt.title("All Planetary Orbits")
    plt.xlabel("X Coordinate (km)")
    plt.ylabel("Y Coordinate (km)")
    plt.axis("equal")  # Keep aspect ratio consistent
    plt.legend()  # Show legend for planet names
    plt.grid()  # Add grid for better visualization
    plt.show() 