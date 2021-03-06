import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")

generator = cms.EDFilter("Pythia8GeneratorFilter",
        comEnergy = cms.double(13000.0),
        crossSection = cms.untracked.double(3.753e-02),
        filterEfficiency = cms.untracked.double(1),
        maxEventsToPrint = cms.untracked.int32(1),
        pythiaHepMCVerbosity = cms.untracked.bool(False),
        pythiaPylistVerbosity = cms.untracked.int32(1),
        PythiaParameters = cms.PSet(
                processParameters = cms.vstring(
                        'Main:timesAllowErrors = 10000',
                        'ParticleDecays:limitTau0 = on',
                        'ParticleDecays:tauMax = 10',
                        'Tune:ee 3',
                        'Tune:pp 5',

                        'NewGaugeBoson:ffbar2Wprime = on',
                        '34:m0 = 2500',
                        '34:onMode = off',
                        '34:onIfAny = 11,12',

                ),
                parameterSets = cms.vstring('processParameters')
        )
)

ProductionFilterSequence = cms.Sequence(generator)
