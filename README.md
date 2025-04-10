# planetary_simulation

# 🌍 Planetary Orbit Simulator

A Python simulation of planetary orbits using classical mechanics and the Runge-Kutta (RK4) method. The system visualizes the orbits of planets around a central star (e.g., the Sun) with matplotlib.

## 🚀 Features

- Models planets using Newtonian gravity
- Integrates equations of motion using RK4
- Generates orbit plots for multiple planets
- Modular and extensible for moons or other bodies

## 🧠 Physics Model

The simulation assumes:
- A central, fixed star (e.g., Sun)
- Circular or elliptical orbits
- 2D Newtonian gravity
- No inter-planetary gravitational effects (for simplicity)

## 📈 Visualization

The simulation uses `matplotlib` to visualize the planetary orbits in 2D space. Planets are represented by their computed trajectories.

## 🛠️ Installation

Clone this repo and install the requirements:

```bash
git clone https://github.com/pyphystuff/planetary_simulation.git
cd planetary_simulation
pip install -r requirements.txt
