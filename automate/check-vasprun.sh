# Author: Rafshan Ul Atik
# Date: 2023
# Email: rafshanulatik@gmail.com

#!/bin/bash

for i in {001..384}; do
    if [ ! -e "dis-$i/vasprun.xml" ]; then
        if [ -e dis-$i/job9*/vasprun.xml ]; then
            cp dis-$i/job9*/vasprun.xml "dis-$i/"
        else
            echo "vasprun.xml not found in dis-$i"
        fi
    fi
done

