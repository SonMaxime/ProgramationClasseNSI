from random import randint
from time import sleep

joueur1 = 0
joueur2 = 0

while True:
    scoreRandom = randint(1, 12)
    joueur1 = joueur1 + scoreRandom

    if joueur1 == 51:
        print("Vous avez gagné.")
        sleep(3)
        break
    elif joueur1 > 51:
        print("Vous avez gagné", scoreRandom)
        sleep(1)
        print("Votre score est de", joueur1, "vous retournez à 25.")
        joueur1 = 25
        sleep(3)