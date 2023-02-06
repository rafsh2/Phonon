# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "arial"
})

# Read the Excel file
df = pd.read_excel('thermal-prop-calc-ZPE.xlsx')

A = df['A']
vib = df['n-TSv']
conf = df['n-TSconf']
temps = df['T(K)']

# Create figure and axes objects
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(temps, A, '-', color='b')
ax.annotate('$\mathrm \Delta_{mix} A$', xy=(1000, A[100]), xytext=(
    10, 3), textcoords='offset points', ha='left', va='center', fontsize=14)  # arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.2'))
ax.plot(temps, vib, '-', color='r')
ax.annotate('$\mathrm -T \Delta_{vib} S$', xy=(1000, vib[100]), xytext=(
    10, 3), textcoords='offset points', ha='left', va='center', fontsize=14)
ax.plot(temps, conf, '-', color='g', label=r'$(\mathrm -T \Delta_{conf} S)$')
ax.annotate('$\mathrm -T \Delta_{conf} S$', xy=(1000, conf[100]), xytext=(
    10, 5), textcoords='offset points', ha='left', va='top', fontsize=14)

ax.set_xlabel('Temperature (K)', fontsize=14)
ax.set_ylabel(r'Helmholtz energy (meV/atom)', fontsize=14)
# ax.legend()

ax.axhline(y=0, color='black', linestyle='dashed',
           alpha=0.6, lw=0.9)  # Plot the zero line
# ax.set_title('volume-temperature', fontsize=18)
ax.set_xlim(0, 1600)
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in", labelsize=12)

plt.savefig('thermal-prop-harm.pdf', bbox_inches='tight')
plt.show()
