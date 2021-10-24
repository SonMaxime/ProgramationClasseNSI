i = 1 # i est le numéro de l'étage
billes = 1000 #nombre de billes initial

while billes > i**2:
    billes = billes - (i**2)
    print("Etage:", i, "Nombre de billes:", i*i)
    i = i + 1 # Je passe à l'étage suivant
print("La pyramide compte", i - 1, "étages.") # i - 1 car on incrémente une dernière fois pour rien