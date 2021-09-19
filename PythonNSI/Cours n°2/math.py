# voir cours 4) la biliothèque maths
from math import sqrt
print("Donnez un nombre dont on souhaite connaitre la racine carré")
nb = int(input("Rentrez votre nombre: "))
rc = sqrt(nb)
print("Nombre de base =", nb, "et le résultat est =", rc)

# quotient et reste d'une division
prixfilm = 8
budget = 102

print("On peut acheter: ", budget / prixfilm, "et il nous restera:", budget % prixfilm)