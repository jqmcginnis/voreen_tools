#!/bin/bash

#SBATCH -J VOREEN_J1
#SBATCH -o jobLog.%j.%N.out 
#SBATCH -D .
#SBATCH --get-user-env
#SBATCH --clusters=cm2_tiny
#SBATCH --partition=cm2_tiny
#SBATCH --mail-type=end
#SBATCH --nodes=1-1
#SBATCH --cpus-per-task=24
#SBATCH --mail-user=julian.mcginnis@tum.de
#SBATCH --export=NONE
#SBATCH --time=01:00:00

module load charliecloud
module load slurm_setup

ch-run  -b /lrz/sys/.:/lrz/sys/ -b /dss/dsshome1/lrz/sys/.:/dss/dsshome1/lrz/sys/ -b $SCRATCH/.:/scratch -w /dss/dsshome1/lxc06/ga82tus2/docker_directory/voreen_without_bindings/ sh /home/voreen-build/bin/run_voreen.sh --no-home





