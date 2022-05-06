#! /usr/bin/env bash
#BATCH --job-name=task1
#SBATCH --partition=sbel
#SBATCH --ntasks=1 --cpus-per-task=1
#SBATCH --time=0-10:30:00
#SBATCH --output="output.txt" --error="output.err"

python3 split.py
