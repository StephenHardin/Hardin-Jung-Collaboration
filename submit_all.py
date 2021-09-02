import subprocess

jobs = len(open("datacard_list.py").readlines(  ))

#range is number of datacards
for count in range(jobs) :
    count += 1
    subprocess.call('sbatch Ntuple_' + str(count) + '.sh', shell=True)

