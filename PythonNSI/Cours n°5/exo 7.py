from random import randint

nombre = randint(1, 100)

while nombre < 100:
    if (nombre + 120) == 4 * nombre:
        print("La somme vaut", nombre)
    nombre = nombre + 1