from random import randint

nbCartesLegendaire = 0

for i in range(1, 101):
    for i in range(5):
        tirage = randint(1, 100)
        if tirage == 1:
            nbCartesLegendaire = nbCartesLegendaire + 1
            print("Vous avez une carte légendaire.")
        elif 2 < tirage < 10:
            print("Vous avez une carte épique.")
        elif 11 < tirage < 30:
            print("Vous avez une carte rare.")
        elif 31 < tirage < 100:
            print("Vous avez une carte commune.")

print("Vous avez", nbCartesLegendaire, "cartes légendaires.")