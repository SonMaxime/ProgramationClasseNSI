nombreElevesClasse = 20

for i in range(10):
    calculNombreFille = (nombreElevesClasse / 4) * 3
    nombreFille = nombreElevesClasse - calculNombreFille
    nombreElevesClasse += 1
    print("Il y a", nombreFille, "filles sur un total de", nombreElevesClasse, "élèves.")