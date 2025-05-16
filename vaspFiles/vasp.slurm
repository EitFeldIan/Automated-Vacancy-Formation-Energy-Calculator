#!/bin/bash
#SBATCH --job-name=4-layer
#SBATCH --account=commons
#SBATCH --partition=commons
#SBATCH --nodes=2
#SBATCH --ntasks-per-node=80
#SBATCH --time=24:00:00
#SBATCH -o logfile
#SBATCH --mem-per-cpu=3G

cd $SLURM_SUBMIT_DIR

echo "Job started on `hostname` at `date`"

module purge
module load intel/2024a
ulimit -s unlimited

srun ~/bin/vasp_std
echo "Job finished on `hostname` at `date`"

