# genproductions


The package includes the datacards used for various generators inclusing POWHEG, MG5_aMC@NLO, Sherpa, Phantom, Pythia...

Further details are reported in the twiki: https://twiki.cern.ch/twiki/bin/view/CMS/GeneratorMain#How_to_produce_gridpacks

Instructions on how to use the fragments are here https://twiki.cern.ch/twiki/bin/view/CMS/GitRepositoryForGenProduction


## Sparse checkout for MG5 tutorial

```
git clone --no-checkout git@github.com:AndreasAlbert/genproductions.git -b 2021-04-22_mg5_tutorial
cd genproductions
git sparse-checkout init --cone
git sparse-checkout set bin/MadGraph5_aMCatNLO/cards/tutorial Utilities  bin/MadGraph5_aMCatNLO/macros bin/MadGraph5_aMCatNLO/patches bin/MadGraph5_aMCatNLO/PLUGIN
```