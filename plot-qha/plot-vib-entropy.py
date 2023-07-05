# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

import matplotlib.pyplot as plt
import pandas as pd

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

# Read the Excel file
xlsx = pd.ExcelFile('thermal_prop_WRe.xlsx')
df_Re = pd.read_excel(xlsx, 'qha-Re96')
df_W = pd.read_excel(xlsx, 'qha-W64')
df_WRe75 = pd.read_excel(xlsx, 'WRe75-qha')
df_WRe50 = pd.read_excel(xlsx, 'WRe50%-qha')

WRe75 = df_WRe75['Sv (meV/K.atom)']
WRe50 = df_WRe50['Sv (meV/K.atom)']
W = df_W['Sv (meV/K.atom)']
Re = df_Re['Sv (meV/K.atom)']
temps = df_W['Temperature (K)']

# Create figure and axes objects
fig, ax = plt.subplots()

ax.plot(temps, WRe50, '-', color='black', lw=1, label='W-50%Re')
ax.plot(temps, WRe75, '-', color='red', lw=1, label='W-25%Re')
ax.plot(temps, W, '-', color='blue', lw=1, label='W')
ax.plot(temps, Re, '-', color='green', lw=1, label='Re')

ax.set_xlabel('Temperature (K)')
ax.set_ylabel(r'$\mathrm {S^{vib}\;(meV/K.atom)}$')
ax.legend()

ax.axhline(y=0, color='black', linestyle='dashed',
           alpha=0.6, lw=0.9)  # Plot the zero line
# ax.set_title('volume-temperature', fontsize=18)
ax.set_xlim(0, 1200)
# ax.set_ylim(0, 1)
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in")

# Shade the region around the intersection temperature
xmin, xmax = 900, 1000
ax.axvspan(xmin, xmax, color='gray', alpha=0.2)
# Add the inset plot
axins = ax.inset_axes([0.55, 0.1, 0.36, 0.45])
axins.plot(temps, WRe50, '-', color='black', lw=1.2, label='W-50%Re')
axins.plot(temps, WRe75, '-', color='red', lw=1.2, label='W-25%Re')
axins.plot(temps, Re, '-', color='green', lw=1.2, label='Re')
axins.plot(temps, W, '-', color='blue', lw=1.2, label='Re')
axins.set_xlim(xmin, xmax)
axins.set_ylim(0.63, 0.71)

axins.set_xticklabels('')
axins.xaxis.set_ticks_position("none")
# axins.yaxis.set_ticks_position("none")
ax.indicate_inset_zoom(axins)
plt.savefig('vib-entropy-qha-modified.pdf', bbox_inches='tight')
plt.show()
