from math import sqrt

somme = 0
n = int(input("Valeur max ? "))

for i in range(1, n + 1):
    somme = somme + (1/i**2)

valeurPI = sqrt(6 * somme)
print(valeurPI)