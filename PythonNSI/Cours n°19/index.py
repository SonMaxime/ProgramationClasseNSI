fic = open('fichier.txt', "w")
fic.write("Wasup, fuckers\n")
ligne = "Salam les reuf"
fic.write(ligne)

for ligne in fic:
    print(ligne)