#!/bin/bash

#SBATCH --account=commons
#SBATCH --partition=scavenge
#SBATCH --nodes=6
#SBATCH --ntasks-per-node=24
#SBATCH --time=4:00:00
#SBATCH -o logfile
cd $SLURM_SUBMIT_DIR

echo "Job started on $(hostname) at $(date)"

# Load necessary modules
module purge
module load intel/2021a

# Run VASP
srun ~/bin/vasp_std

echo "Job finished on $(hostname) at $(date)"
