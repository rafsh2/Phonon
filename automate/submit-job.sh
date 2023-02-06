# Author: Rafshan Ul Atik
# Date: 2022
# Email: rafshanulatik@gmail.com

#!/usr/bin/bash

# loop through numbers 372 to 380
for i in {372..380}
do

    # submit job script "job.sh" in the directory with name "dis-<number>"
    # using the qsub command
    qsub dis-$i/job.sh
  
done

