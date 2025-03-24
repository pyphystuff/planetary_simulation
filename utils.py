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


def plot_orbit(distance):
    # Generate data for the orbit (circle)
    theta = [i * 0.01 for i in range(0, 628)]  # 0 to 2π in small steps
    x = [distance * math.cos(t) for t in theta]
    y = [distance * math.sin(t) for t in theta]
    plt.plot(x, y, label=f"Orbit at {distance} km")
    plt.title("Planetary Orbit Visualization")
    plt.xlabel("X Coordinate (km)")
    plt.ylabel("Y Coordinate (km)")
    plt.legend()
    plt.axis("equal")  # Keep aspect ratio
    plt.grid()

# Ensure to display the plot after all orbits are drawn
    plt.show()