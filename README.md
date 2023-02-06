 Automate
============
Phonopy will generate a lot of single atom displacement files depending on the symmetry of the input lattice.These are few bash script that performs several tasks, including creating directories, moving and copying those displacement files, and finally submitting job scripts to a job scheduler of the cluster.

## Usage

To run the script, make sure the script file is executable (e.g., `chmod 700 scf-dir.sh`)

## Limitations
* The script assumes that the four files (`POTCAR`, `INCAR`, `KPOINTS`, `job.sh`) are in the current directory.
* The script assumes that the job scheduler accepts the `qsub` command to submit job scripts.
* The script assumes that the job scheduler uses the `job.sh` file as the job script file.

