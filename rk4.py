import numpy as np
import matplotlib.pyplot as plt

# Physical Constants
G = 6.67430e-11  # Gravitational constant (m³/kg/s²)
M_sun = 1.989e30  # Mass of the Sun (kg)
AU = 1.496e11  # 1 Astronomical Unit (m)
year = 3.154e7  # 1 year in seconds

# Time step and duration
dti = 24 * 3600  # 1 day in seconds
stepsi = 365 * 5  # Simulate 5 years

# Initial conditions for Earth
xi, yi = AU, 0  # Start at 1 AU from the Sun
#vxi, vyi = 0, 29780  # Earth's velocity in m/s (approximate circular orbit)
vxi, vyi = 0, 29780

def acceleration(x, y):
    """Compute acceleration due to Sun's gravity."""
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


#print(rk4(xi,yi,vxi,vyi,dti,stepsi))

x_list2,y_list2 = rk4(xi,yi,vxi,vyi,dti,stepsi)

### definir objetos con velocidad y distancias reales




# Plot the orbit
plt.figure(figsize=(6,6))
plt.plot(x_list2, y_list2, label="Earth's Orbit")
plt.scatter(0, 0, color='orange', label="Sun", s=200)
plt.xlabel("x [m]")
plt.ylabel("y [m]")
plt.title("Earth Orbiting the Sun using RK4")
plt.legend()
plt.grid()
plt.axis("equal")
plt.show()
