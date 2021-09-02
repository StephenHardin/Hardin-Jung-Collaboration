i     = 0
f     = open('datacard_list.py', 'r')
lines = f.readlines()


for line in lines :
    i   += 1
    lines = line.strip('\n')
    sh_file = 'Ntuple_' + str(i) + '.sh'
    
    with open(sh_file, 'w') as cfg :
        cfg.write("#!/bin/sh")
        cfg.write("\n")
        cfg.write("#SBATCH  -A cms-a")
        cfg.write("\n")
        cfg.write("#SBATCH --nodes=1")
        cfg.write("\n")
        cfg.write("#SBATCH --time=00:15:00")
        cfg.write("\n")
        cfg.write("cd /home/hardin24/CMSSW_10_2_13/src/")
        cfg.write("\n")
        cfg.write("source /cvmfs/cms.cern.ch/cmsset_default.sh")
        cfg.write("\n")
        cfg.write("export SCRAM_ARCH=slc6_amd64_gcc530")
        cfg.write("\n")
        cfg.write("eval `scramv1 runtime -sh`")
        cfg.write("\n")
        cfg.write("combine -M AsymptoticLimits "+str(line) + " --toys 10000")
        #print("combine -M AsymptoticLimits "+str(line) + " --toys 10000")
        cfg.write("\n")
