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

dopantJSON=$(echo "$path" | awk -F'/' '{OFS="/"; $0=$0; NF-=2; print}').json

python3 - <<EOF
import json

with open("${dopantJSON}", 'r') as file:
    dopant = json.load(file)
    dopant.updateStatus("${SLURM_SUBMIT_DIR}", "Started")

EOF


echo "Job started on `hostname` at `date`"

module purge
module load intel/2024a
ulimit -s unlimited

srun ~/bin/vasp_std
echo "Job finished on `hostname` at `date`"

python3 - <<EOF
import json

with open("${dopantJSON}", 'r') as file:
    dopant = json.load(file)
    dopant.updateStatus("${SLURM_SUBMIT_DIR}", "Finished")

EOF

