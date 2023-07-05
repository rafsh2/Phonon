# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

#! /bin/bash
for i in {001..384}
do
    if [ ! -e "dis-$i" ]; then
    # if the file doesn't exist, skip this iteration
        continue
    fi
    cd dis-$i
    if [ -e job9*/vasprun.xml ];
    then
    cp job*/vasprun.xml .
    else 
    echo $(pwd)
    fi
    cd ..
done
