import os

# signal grid points
masses = ["1000"]
couplingarrays = [["0.1", "0.5", "1.0"],
                  ["1.0", "0.5", "0.1"]]

for mass in masses: # iterate over masses
  for couplingarray in couplingarrays: # iterate over couplings

    # replace . to p since . in the gridpacks cause problems in McM
    gridname = "ZprimeToLL-M{0}-g{1}-reweight".format(mass,couplingarray[0].replace(".", "p"))

    # check if the directory already exists
    if os.path.exists("{0}".format(gridname)):
      print "Directory already exists {0}".format(gridname)
      print " >> Skipping this mass/coupling grid"
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
    os.system("sed -i 's|###coupling###|{0}|g' {1}/{2}_customizecards.dat".format(couplingarray[0],gridname,gridname))

    # need to create reweight_card
    reweight_card = open("{0}/{1}_reweight_card.dat".format(gridname,gridname), "w")
    reweight_card.write("change rwgt_dir rwgt\n")

    for i_coupling in range(1,len(couplingarray)):
      coupling = couplingarray[i_coupling]
      reweight_card.write("launch --rwgt_name=g{0}\n".format(coupling.replace(".", "p")))
      reweight_card.write("set param_card gvd11 {0}\n".format(coupling))
      reweight_card.write("set param_card gvd22 {0}\n".format(coupling))
      reweight_card.write("set param_card gvd33 {0}\n".format(coupling))
      reweight_card.write("set param_card gvu11 {0}\n".format(coupling))
      reweight_card.write("set param_card gvu22 {0}\n".format(coupling))
      reweight_card.write("set param_card gvu33 {0}\n".format(coupling))
      reweight_card.write("set param_card gVl11 {0}\n".format(coupling))
      reweight_card.write("set param_card gVl22 {0}\n".format(coupling))
      reweight_card.write("set param_card gVl33 {0}\n".format(coupling))
      reweight_card.write("set WY1 AUTO\n\n")
    reweight_card.close()
