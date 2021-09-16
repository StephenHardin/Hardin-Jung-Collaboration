#!/bin/sh
import subprocess

jobs = len(open("Datacard_list.txt").readlines(  ))

#range is number of datacards
for count in range(1,jobs+1) :
    count += 1
    subprocess.call('sbatch Ntuple_' + str(count) + '.sh', shell=True)

