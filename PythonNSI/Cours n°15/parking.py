from random import randint

parking = []

for i in range(10):
    h = randint(1, 2)
    if h == 1:
        parking.append("D")
    elif h == 2:
        parking.append("V")

def afficher_parking():
    print(parking)

afficher_parking()