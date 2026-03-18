import numpy as np
import matplotlib.pyplot as plt
k = 401 # W /(m K)
h = 10 # W / (m^2 K)
T0 = 400 # K
Ta = 300 # K

r_solid = 0.01 # m
R_hollow = 0.01 # m
r_hollow = 0.005 # m

A_solid = np.pi * r_solid**2 # m^2
A_hollow = np.pi * (R_hollow**2 - r_hollow**2) # m^2

P_solid = 2 * np.pi * r_solid # m
P_hollow = 2 * np.pi * R_hollow # m

m_solid = (h * P_solid)/(k * A_solid) # m^-2
m_hollow = (h * P_hollow)/(k * A_hollow) # m^-2

x = np.linspace(0, 1, 200) # m

T_solid = Ta + ((T0 - Ta) * np.exp(-np.sqrt(m_solid)*x)) # K
T_hollow = Ta + ((T0 - Ta) * np.exp(-np.sqrt(m_hollow)*x)) # K

figure, axes = plt.subplots(2, 1)
axes[0].plot(x, T_solid, color="red")
axes[0].set_title("Temperature Distribution Along a Solid Copper Rod", family = "arial")
axes[0].set_xlabel("Distance Along the Rod (m)", family = "arial")
axes[0].set_ylabel("Temperature (K)", family = "arial")
axes[0].legend(["Solid"])
axes[0].grid(True)

axes[1].plot(x, T_hollow, color="orange")
axes[1].set_title("Temperature Distribution Along a Hollow Copper Rod", family = "arial")
axes[1].set_xlabel("Distance Along the Rod (m)", family = "arial")
axes[1].set_ylabel("Temperature (K)", family = "arial")
axes[1].legend(["Hollow"])
axes[1].grid(True)

plt.tight_layout()
plt.savefig("temperature_distribution.png", dpi=300)
plt.show()