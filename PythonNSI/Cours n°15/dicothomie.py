# Remplissage d'une liste avec 20 éléments
from random import randint

liste = []

for i in range(20):
    liste = liste + [randint(1, 101)]
liste.sort()
print(liste)

# Recherche par dichotomie

x = 6 # Nombre recherché
position = None
fini = None
debut = 0
fin = len(liste) - 1
milieu = (debut + fin) / 2

while fini != True:
    if x < liste[milieu]: # Partie gauche de la liste
        fin = milieu - 1
    elif x > liste[milieu]: # Partie droite de la liste
        debut = milieu + 1
    elif x == liste[milieu]: 
        position = milieu
        fini = True