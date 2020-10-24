spin = input()
electric_charge = input()

if spin == "1":
    if electric_charge == "0":
        particle = "Photon"
        class_ = "Boson"
elif spin == "1/2":
    if electric_charge == "-1/3":
        particle = "Strange"
        class_ = "Quark"
    elif electric_charge == "2/3":
        particle = "Charm"
        class_ = "Quark"
    elif electric_charge == "-1":
        particle = "Electron"
        class_ = "Lepton"
    elif electric_charge == "0":
        particle = "Neutrino"
        class_ = "Lepton"


print(particle + " " + class_)
