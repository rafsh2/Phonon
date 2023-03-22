# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the license specified in the LICENSE file.

import re
import numpy as np
from scipy.interpolate import interp1d
import csv

data = {}  # Initialize empty dictionary to store data
skip = True  # Initialize skip flag to skip first line after temperature line

with open('entropy-volume.dat', 'r') as file:
    for line in file:
        if re.match(r'# temperature', line):
            temp = float(line.split()[2])  # Extract temperature value
            data[temp] = []  # Initialize empty list for current temperature
            skip = True  # Skip first line after temperature line
        elif line.strip() and not skip:  # Check if line is not empty and not to be skipped
            # Extract data values and append to list for current temperature
            values = [float(x) for x in line.split()]
            data[temp].append(values)
        else:
            skip = False

# read temperature and volume data from .dat file
temp, vol = np.loadtxt('volume-temperature.dat', unpack=True)

# create empty list to store results
result = []

# iterate over temperature and volume data
for t, v in zip(temp, vol):
    # find corresponding entropy value in dictionary
    data_list = data.get(t)
    if data_list is None:
        continue
    vol_data = [item[0] for item in data_list]
    entr_data = [item[1] for item in data_list]
    f = interp1d(vol_data, entr_data, kind='cubic', fill_value='extrapolate')
    entr = f(v)
    result.append([t, v, entr])

# Write the result to a csv file
with open('temp-vol-entr.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Temperature', 'Volume', 'Entropy'])
    for row in result:
        writer.writerow(row)
