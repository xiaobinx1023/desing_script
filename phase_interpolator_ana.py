import numpy as np
import matplotlib.pyplot as plt
import pdb
# Define the range for theta1 and theta2
theta1 = np.linspace(0, 2 * np.pi, 100)
theta2 = np.linspace(0, 2 * np.pi, 100)
theta1, theta2 = np.meshgrid(theta1, theta2)
omega = np.linspace(1, 100e9, 10000) * 2 * np.pi # frequency of interest
delay = 25e-12 # delay between different phases
delta_theta = omega * delay # phase delay between different phases


# 
shape = np.shape(delta_theta)
# Strength of two clock phase A and  B, A + B = Idenity
Alin = np.linspace(0, 1, 101)
Blin = np.ones(np.shape(Alin)) - Alin

# pdb.set_trace()
# Calculate the magnitude |C| and phase 
C_magnitude = np.empty(delta_theta.shape + Alin.shape)
C_phase = np.empty(delta_theta.shape + Alin.shape)
for idx_ in range(Alin.shape[0]):
    C_magnitude[:, idx_] = np.sqrt(Alin[idx_] ** 2 + Blin[idx_] ** 2 + 2*Alin[idx_] * Blin[idx_] * np.cos(delta_theta))

    C_phase[:, idx_] = np.arctan2(Blin[idx_] * np.sin(delta_theta), (Alin[idx_] + Blin[idx_]) * np.cos(delta_theta))

# Plot the magnitude
fig = plt.figure()
Alin, omega = np.meshgrid(Alin, omega)
# pdb.set_trace()

ax = fig.add_subplot(121, projection='3d')
ax.plot_surface(Alin, omega, C_magnitude, cmap='viridis')
ax.set_title('Magnitude |C|')
ax.set_xlabel('Alin')
ax.set_ylabel('omega')
ax.set_zlabel('|C|')

# Plot the phase
ax2 = fig.add_subplot(122, projection='3d')
ax2.plot_surface(Alin, omega, C_phase, cmap='viridis')
ax2.set_title('Phase arg(C)')
ax2.set_xlabel('Alin')
ax2.set_ylabel('Omega')
ax2.set_zlabel('arg(C)')

plt.show()