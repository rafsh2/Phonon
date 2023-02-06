# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "arial"
})
# Read data from .dat file
data = np.loadtxt('thermal_expansion.dat')

# Create figure and axes objects
fig, ax = plt.subplots(figsize=(8, 6))

# Plot the data
ax.plot(data[:, 0], data[:, 1], '-', color='r', label='Data')

# Add axis labels and title
ax.set_xlabel('Temperature (K)', fontsize=14)
ax.set_ylabel(r'Thermal expansion $(\mathrm{K}^{-1})$', fontsize=14)
# ax.set_title('volume-temperature', fontsize=18)
ax.set_xlim(data[0, 0], data[-1, 0])

# Add grid and legend
# ax.grid(True)
# ax.legend(loc='best')

# Set tick parameters
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in", labelsize=12)

# Save the figure
plt.savefig('thermal_expansion.pdf', bbox_inches='tight')
plt.show()
