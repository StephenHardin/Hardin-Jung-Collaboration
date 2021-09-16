import subprocess

jobs = len(open("Datacard_list.txt").readlines(  ))

#range is number of datacards
for count in range(jobs) :
    count += 1
    subprocess.call('sbatch Ntuple_' + str(count) + '.sh', shell=True)

