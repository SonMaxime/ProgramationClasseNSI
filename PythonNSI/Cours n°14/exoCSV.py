import csv
fichier = open(r"villes-france.csv")
données = csv.reader(fichier)

liste = []
for éléments in données:
    liste = liste + éléments

if "rethel" in liste:
    print("Rethel est dans la liste")
else:
    print("Rethel n'es pas dans la liste")

print("Il y a", len(liste), "villes en France")
print(données.loc[25537])