# ON veut calculer l'hypoténuse d'un triangle.

from math import sqrt
a = float(input("valeur de A: "))
b = float(input("valeur de B: "))
c = sqrt(a**2 + b**2)
c = round(c, 1) #arondis le resultat à 1 chiffre après la virgule
print("L'hypoténuse vaut", c)