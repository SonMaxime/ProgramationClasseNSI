from random import randint

nombreDeFoisSix = 0
n = int(input("Indiquez le nombre de lancers: "))

for i in range(1, n + 1):
    rand = randint(1, 6)
    if rand == 6:
        nombreDeFoisSix = nombreDeFoisSix + 1

print("Vous avez eu", nombreDeFoisSix, "fois le nombre 6.")