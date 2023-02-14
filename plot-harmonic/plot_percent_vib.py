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

vib = df['%Vib']
conf = df['%Conf']
temps = df['T(K)']

# Create figure and axes objects
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(temps, vib, '-', color='r')
ax.annotate('$\mathrm \% \Delta_{vib} S$ in $\mathrm \Delta_{mix} S$', xy=(800, vib[180]), xytext=(
    10, 18), textcoords='offset points', ha='left', va='top', fontsize=14)
ax.plot(temps, conf, '-', color='g', label=r'$(\mathrm -T \Delta_{conf} S)$')
ax.annotate('$\mathrm \% \Delta_{conf} S$ in $\mathrm \Delta_{mix} S$', xy=(800, conf[180]), xytext=(
    10, 18), textcoords='offset points', ha='left', va='top', fontsize=14)

ax.set_xlabel('Temperature (K)', fontsize=14)
# ax.set_ylabel(r'Helmholtz energy (meV/atom)', fontsize=14)
# ax.legend()

# ax.set_title('volume-temperature', fontsize=18)
ax.set_xlim(0, 1600)
ax.set_ylim(0, 100)
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in", labelsize=12)
ax.set_yticks([y for y in ax.get_yticks() if y != 0])

plt.savefig('percent-vib.pdf', bbox_inches='tight')
plt.show()
