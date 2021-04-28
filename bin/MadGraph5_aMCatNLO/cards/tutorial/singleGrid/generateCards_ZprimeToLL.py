import os

# signal grid points
masses = ["1000"]
couplings = ["0.1", "0.2", "0.5", "1.0"]

for mass in masses: # iterate over masses
  for coupling in couplings: # iterate over couplings

    # replace . to p since . in the gridpacks cause problems in McM
    gridname = "ZprimeToLL-M{0}-g{1}".format(mass,coupling.replace(".","p"))

    # check if the directory already exists
    if os.path.exists("{0}".format(gridname)):
      print "Directory already exists {0}".format(gridname)
      print "Skipping this mass/coupling grid"
      continue

    print "Generating cards for {0}".format(gridname)
    os.system("mkdir {0}".format(gridname))

    # no need to change extramodels and run_card
    os.system("cp skeleton/ZPrimeToLL_extramodels.dat {0}/{1}_extramodels.dat".format(gridname,gridname))
    os.system("cp skeleton/ZPrimeToLL_run_card.dat {0}/{1}_run_card.dat".format(gridname,gridname))

    # need to change proc_card => output name
    os.system("cp skeleton/ZPrimeToLL_proc_card.dat {0}/{1}_proc_card.dat".format(gridname,gridname))
    os.system("sed -i 's|###output###|{0}|g' {1}/{2}_proc_card.dat".format(gridname,gridname,gridname))

    # need to change customizecards => masses and couplings
    os.system("cp skeleton/ZPrimeToLL_customizecards.dat {0}/{1}_customizecards.dat".format(gridname,gridname))
    os.system("sed -i 's|###mass###|{0}|g' {1}/{2}_customizecards.dat".format(mass,gridname,gridname))
    os.system("sed -i 's|###coupling###|{0}|g' {1}/{2}_customizecards.dat".format(coupling,gridname,gridname))

