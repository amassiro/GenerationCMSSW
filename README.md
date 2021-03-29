# GenerationCMSSW

Some EFT specific in 

    https://github.com/UniMiBAnalyses/CMSSWGeneration

Here the generic procedure, from Raffaele Gerosa instructions

    https://gitlab.cern.ch/UCSD-CMS-Analyses/generationprivatemc/-/tree/master/Era_2016/EWK_LLJJ_madgraph_pythia_recoilON
    

Instructions: 

    ssh lxplus6
    cd <local directory where jobs need to be created>
    git clone git@github.com:amassiro/GenerationCMSSW.git GenerationCMSSW
    cd GenerationCMSSW/Era_2017/EWZ_LVJJ_madgraph_pythia_recoilON
    cmsrel <CMSSW release needed for miniAOD step>
    cd <CMSSW release>/src
    cmsenv
    cd -
    source /cvmfs/cms.cern.ch/common/crab-setup.sh
    voms-proxy init -voms cms
    crab submit crabConfig.py

    
    
    
    
    



