import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "pdf.fonttype": 42,
    "font.size": 12,
     "axes.labelsize": 18,
})

# Read the Excel file
df = pd.read_excel('thermal_prop_WRe.xlsx', sheet_name='75-qha')

A = df['A']
Ac = df['A (conf)']
vib = df['n-TSv']
conf = df['n-TSconf']
temps = df['T(K)']

# Create figure and axes objects
fig, ax = plt.subplots()

# ax.plot(temps, A, '-', color='b')
# ax.annotate('$\mathrm {\Delta_{mix} G}$', xy=(420, A[45]), xytext=(
#     10, 3), textcoords='offset points', ha='left', va='center')
ax.plot(temps, Ac, '--', color='b')
ax.annotate('$\mathrm {\Delta_{mix} G}$', xy=(800, A[48]), xytext=(
    10, 3), textcoords='offset points', ha='left', va='center')
# ax.plot(temps, vib, '-', color='r')
# ax.annotate('$\mathrm {-T \Delta_{mix} S^{vib}}$', xy=(300, vib[33]), xytext=(
#     10, 3), textcoords='offset points', ha='left', va='center')
ax.plot(temps, conf, '-', color='g')
ax.annotate('$\mathrm {-T \Delta_{mix} S^{conf}}$', xy=(650, conf[109]), xytext=(
    10, 5), textcoords='offset points', ha='left', va='top')

ax.set_xlabel('Temperature (K)')
ax.set_ylabel(r'Gibbs energy (meV/atom)')
# ax.legend()

ax.axhline(y=0, color='black', linestyle='dashed',
           alpha=0.6, lw=1)  # Plot the zero line
ax.set_xlim(0, 1600)
ax.xaxis.set_ticks_position("both")
ax.yaxis.set_ticks_position("both")
ax.tick_params(axis='both', which='major', direction="in")

intersection_point = (0, A[0])
ax.plot(*intersection_point, marker='o', markersize=3, color='k')
ax.annotate(r'$\mathrm{\Delta_{mix}H}$', xy=intersection_point, xytext=(60, -2),
            textcoords='offset points', ha='right', va='center', arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=0.2'), fontsize=12)

indices = [i for i in range(1, len(Ac)) if (Ac[i-1] > 0 and Ac[i] <= 0)]
if len(indices) == 0:
    print("A does not cross zero between the given temperature points.")
else:
    for index in indices:
        t0, t1 = temps[index-1], temps[index]
        a0, a1 = Ac[index-1], Ac[index]
        A_zero_temp = t0 - ((t0 - t1) / (a0 - a1)) * a0

ax.axvline(x=A_zero_temp, color='black', linestyle='dashed', alpha=0.5, lw=0.9)
ax.annotate(f'T = {int(A_zero_temp)} K', xy=(A_zero_temp, -80), xytext=(5, 5),
            textcoords='offset points', ha='left', va='bottom')

plt.savefig('thermal-prop-qha-conf-WRe75.jpg', bbox_inches='tight')
plt.show()
