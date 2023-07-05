# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
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
WRe50_data = np.loadtxt('total_dos-WRe50-1.dat')
WRe75_data = np.loadtxt('total_dos-WRe75.dat')
W_data = np.loadtxt('total_dos-W.dat')
Re_data = np.loadtxt('total_dos-Re.dat')

# Create figure and axes objects
fig, ax = plt.subplots()

# Plot the data
ax.plot(WRe50_data[:,0], (WRe50_data[:,1]/64), color='black', linestyle='-', label='W-50%Re')
ax.plot(WRe75_data[:,0], (WRe75_data[:,1]/64), color='red', linestyle='-', label='W-25%Re')
ax.plot(W_data[:,0], (W_data[:,1]/64), color='blue', linestyle='-', label='W')
ax.plot(Re_data[:,0], (Re_data[:,1]/96), color='green', linestyle='-', label='Re')

ax.fill_between(WRe50_data[:,0], 0, (WRe50_data[:,1]/64), alpha=0.15, color='black')
ax.fill_between(WRe75_data[:,0], 0, (WRe75_data[:,1]/64), alpha=0.15, color='red')
ax.fill_between(W_data[:,0], 0, (W_data[:,1]/64), alpha=0.15, color='blue')
ax.fill_between(Re_data[:,0], 0, (Re_data[:,1]/96), alpha=0.15, color='green')

# Add axis labels and title
ax.set_xlabel('Frequency (THz)')
ax.set_ylabel('Phonon DOS (states/THz.atom)')
# plt.ylim(0, 2.1)
ax.set_ylim(bottom=0)
ax.legend(loc='best')

# Set tick parameters
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in")
formatter = ticker.FormatStrFormatter('%d')
ax.yaxis.set_major_locator(ticker.MaxNLocator(integer=True))
ax.yaxis.set_major_formatter(formatter)
# Save the figure
plt.savefig('total-dos.pdf', bbox_inches='tight')
plt.show()
