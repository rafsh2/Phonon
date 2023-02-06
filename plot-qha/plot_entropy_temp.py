# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

import matplotlib.pyplot as plt
import pandas as pd

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "arial"
})

# Read the Excel file after converting from csv in the units of your choice.
# Change the file/header names as you wish.

df = pd.read_excel('output-qha-WRe.xlsx')
temps = df['Temperature']
entropies = df['Sv (meV/K.atom)']

# Superimpose entropy from harmonic calc
df = pd.read_excel('output-WRe64.xlsx')

temp_harm = df['temperature']
entropy_harm = df['Sv(mev/K.atom)']

# Create figure and axes objects
fig, ax = plt.subplots(figsize=(8, 6))

ax.plot(temps, entropies, '-', color='r', label='Quasiharmonic', lw=0.9)
ax.plot(temp_harm, entropy_harm, '-', color='b', label='Harmonic', lw=0.9)
ax.set_xlabel('Temperature (K)', fontsize=14)
ax.set_ylabel(r'Vibrational entropy (meV/atom)', fontsize=14)
ax.legend()
# ax.set_title('volume-temperature', fontsize=18)
ax.set_xlim(0, 1600)
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in", labelsize=12)

plt.savefig('entropy-temperature.pdf', bbox_inches='tight')
plt.show()
