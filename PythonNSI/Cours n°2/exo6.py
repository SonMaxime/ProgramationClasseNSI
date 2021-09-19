# On veut le nombre d'heures, de minutes et de secondes dans 8000 secondes (à corriger)

from math import * 

nombre_secondes = 8000
heures = nombre_secondes // 3600
reste_heure = nombre_secondes % 3600
minutes = int(reste_heure / 60)

print("Dans", nombre_secondes, "secondes , il y a:", heures, "heures, ", minutes, "minutes et il reste:", reste_heure)