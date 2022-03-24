from time import time
from random import randint
liste = []
debut = time()
for i in range(1001):
    nombre = randint(1, 10000)
    liste.append(nombre)
n = len(liste)

for y in range(0, n - 1):
    liste_min = y
    for z in range(y + 1, n):
        if liste[z] < liste[liste_min]:
            liste_min = z
    if liste_min != y:
        temp = liste[liste_min]
        liste[liste_min] = liste[i]
        liste[i] = temp

print(liste)