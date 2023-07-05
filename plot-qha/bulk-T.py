# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    # "text.usetex": True,
    "font.family": "Times New Roman",
    "pdf.fonttype": 42,
    "font.size": 14,
    "axes.labelsize": 18,
    'axes.linewidth': 1.5,
    'xtick.major.width': 1.5,
    'ytick.major.width': 1.5
})
# Read data from .dat file
WRe50_data = np.loadtxt('bulk_modulus-temperature-WRe50.dat')
WRe75_data = np.loadtxt('bulk_modulus-temperature-WRe75.dat')
W_data = np.loadtxt('bulk_modulus-temperature-W.dat')
Re_data = np.loadtxt('bulk_modulus-temperature-Re.dat')

# Create figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(WRe50_data[:,0], WRe50_data[:,1], color='red', linestyle='-', label='WRe alloys')
# ax.plot(WRe75_data[:,0], WRe50_data[:,1], color='purple', linestyle='-', label=r'$\mathrm{W_{0.75}Re_{0.25}}$')
ax.plot(W_data[:,0], W_data[:,1], color='blue', linestyle='-', label='W')
ax.plot(Re_data[:,0], Re_data[:,1], color='green', linestyle='-', label='Re')

# Add axis labels and title
ax.set_xlabel('Temperature (K)')
ax.set_ylabel('Bulk Modulus (GPa)')
# ax.set_title('volume-temperature', fontsize=18)
ax.set_xlim(WRe50_data[0, 0], WRe50_data[-1, 0])

# Add grid and legend
# ax.grid(True)
ax.legend(loc='best')

# Set tick parameters
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in")

# Save the figure
plt.savefig('bulk_modulus-temperature.pdf', bbox_inches='tight')
plt.show()
