import math
import matplotlib.pyplot as plt
import numpy as np

##constants
G = 6.67430e-11  # Gravitational constant
steps = 5000
dt= 0.01
M_sun = 1.989e30
#x, y = 1.0, 0.0  # Initial position (1 AU from the Sun)
#vx, vy = 0.0, 1.0  # Initial velocity (circular orbit)

def calculate_gravitational_force(m1, m2, distance):
    if distance == 0:
        return 0
    return G * (m1 * m2) / (distance**2) 

#acceltaration for rk4

def acceleration(x, y):
    """Compute acceleration due to gravity."""
    r = np.sqrt(x**2 + y**2)
    ax = -G * M_sun * x / r**3
    ay = -G * M_sun * y / r**3
    return ax, ay


# RK4 Method
def rk4(x,y,vx,vy,dt,steps):    ##initial conditions
    x_list, y_list = [x], [y]
    for _ in range(steps):
        
        ax1, ay1 = acceleration(x, y)
        k1vx, k1vy = ax1 * dt, ay1 * dt
        k1x, k1y = vx * dt, vy * dt

        ax2, ay2 = acceleration(x + k1x/2, y + k1y/2)
        k2vx, k2vy = ax2 * dt, ay2 * dt
        k2x, k2y = (vx + k1vx/2) * dt, (vy + k1vy/2) * dt

        ax3, ay3 = acceleration(x + k2x/2, y + k2y/2)
        k3vx, k3vy = ax3 * dt, ay3 * dt
        k3x, k3y = (vx + k2vx/2) * dt, (vy + k2vy/2) * dt

        ax4, ay4 = acceleration(x + k3x, y + k3y)
        k4vx, k4vy = ax4 * dt, ay4 * dt
        k4x, k4y = (vx + k3vx) * dt, (vy + k3vy) * dt

        # Update position and velocity
        x += (k1x + 2*k2x + 2*k3x + k4x) / 6
        y += (k1y + 2*k2y + 2*k3y + k4y) / 6
        vx += (k1vx + 2*k2vx + 2*k3vx + k4vx) / 6
        vy += (k1vy + 2*k2vy + 2*k3vy + k4vy) / 6
        x_list.append(x)
        y_list.append(y)

    return x_list,y_list

##updating positions
def plot_all_orbits(planets):
    dti = 24 * 3600  # 1 day in seconds
    stepsi = 365 * 200  # Simulate 5 years
    for planet in planets:
        # Convert km to m and km/s to m/s
        distance_m = planet.distance_from_star * 1e3
        velocity_m_s = planet.velocity * 1e3
        x_list2, y_list2 = rk4(distance_m, 0.0, 0.0, velocity_m_s, dti, stepsi)

        plt.plot(x_list2, y_list2, label=planet.name)

    plt.title("All Planetary Orbits")
    plt.xlabel("X Coordinate (m)")
    plt.ylabel("Y Coordinate (m)")
    plt.axis("equal")
    plt.legend()
    plt.grid()
    plt.show()


