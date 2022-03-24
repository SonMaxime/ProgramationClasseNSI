from random import randint

liste = []

for i in range(20000):
    nb = randint(1, 4)
    if nb == 1:
        liste.append("C")
    elif nb == 2:
        liste.append("G")
    elif nb == 3:
        liste.append("T")
    elif nb == 4:
        liste.append("U")

nbSequences = 0

for i in range(0, 500):
    if ['C', 'C', 'C', 'C', 'C'] in liste:
        nbSequences =+ 1

if nbSequences < 5:
    print("La personne est infectée.", nbSequences)
else:
    print("La personne n'est pas infectée.")
