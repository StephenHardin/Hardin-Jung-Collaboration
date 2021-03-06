i     = 0
f     = open('Datacard_list.txt', 'r')
lines = f.readlines()


for line in lines :
    i   += 1
    lines = line.strip('\n')
    sh_file = 'Ntuple_' + str(i) + '.sh'
    
    with open(sh_file, 'w') as cfg :
        line = line.strip('\n')
        cfg.write("#!/bin/sh")
        cfg.write("\n")
        cfg.write("#SBATCH  -A cms")
        cfg.write("\n")
        cfg.write("#SBATCH --nodes=1")
        cfg.write("\n")
        cfg.write("#SBATCH --time=30:00:00")
        cfg.write("\n")
        cfg.write("cd /home/hardin24/CMSSW_10_2_13/src/Hardin-Jung-Collaboration")
        cfg.write("\n")
        cfg.write("source /cvmfs/cms.cern.ch/cmsset_default.sh")
        cfg.write("\n")
        cfg.write("export SCRAM_ARCH=slc6_amd64_gcc530")
        cfg.write("\n")
        cfg.write("eval `scramv1 runtime -sh`")
        cfg.write("\n")
        cfg.write("combine -M AsymptoticLimits "+str(line)+" --toys 100000")
        cfg.write("\n")
