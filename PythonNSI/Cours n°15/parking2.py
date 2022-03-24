from random import randint
place = ["d"] * 10

while True:
    a = int(input("Bienvenue au niveau -1, que souhaitez vous faire.\n1. Afficher la liste des places disponibles\n2. Garer sa voiture\n3. Sortir la voiture\nVotre choix:"))
    if a == 1:
        for i in range(10):
            n = randint(0, 9)
            if place[n] == 'd':
                print("Place", i, ": Disponible.")
            elif place[n] == 'o':
                print("Place", i, ": Occupée.")
    elif a == 2:
        for i in range(10):
            n = randint(0, 9)
            if place[n] == 'd':
                place[n] = 'o'
                print("Votre voiture est garé.\n")
                break
    elif a == 3:
        for i in range(10):
            n = randint(0, 9)
            if place[n] == 'o':
                place[n] = 'd'
                print("Votre voiture a été sortie.\n")
                break