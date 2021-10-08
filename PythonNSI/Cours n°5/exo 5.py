epaisseur = 0.1
toureffel = 324000
nbpliures = 0
# Quand on plie, l'épaisseur est doublé.

while epaisseur < toureffel:
    epaisseur = epaisseur * 2
    nbpliures = nbpliures + 1
print("Il faut", nbpliures, "pliures pour que la feuille fasse la hauteur de la tour effel")