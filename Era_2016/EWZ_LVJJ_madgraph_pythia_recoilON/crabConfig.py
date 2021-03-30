from CRABClient.UserUtilities import config
config = config()

config.General.requestName     = 'rgerosa_EWK_LJJ_2016_powheg_pythia_dipole'
config.General.workArea        = 'crab_EWK_LJJ_2016_powheg_pythia_dipole'
config.General.transferOutputs = True
config.General.transferLogs    = False

config.JobType.pluginName  = 'PrivateMC'
config.JobType.psetName    = 'miniAOD_step_fake.py'
config.JobType.maxMemoryMB = 3000
config.JobType.inputFiles  = ['scriptExe.sh', 'genSim_step.py','digiRaw_step.py','recoAOD_step.py','miniAOD_step.py','pileup.py','LJJ_EWK_MLL_105-160_slc6_amd64_gcc630_CMSSW_9_3_16_tarball.tar.xz']
config.JobType.scriptExe   ='scriptExe.sh'
config.JobType.numCores    = 2

config.Data.splitting   = 'EventBased'
config.Data.unitsPerJob = 500
config.Data.totalUnits  = 2000000
config.Data.outLFNDirBase = '/store/user/rgerosa/PrivateMC'
config.Data.publication   = True
config.Data.outputPrimaryDataset = 'EWK_LJJ_MLL_105-160_TuneCP5_13TeV-madgraph-pythia_dipole'
config.Data.outputDatasetTag     = 'RunIISummer16MiniAODv3-PUMoriond17_94X_mcRun2_asymptotic_v3'

config.Site.storageSite = 'T2_US_UCSD'
