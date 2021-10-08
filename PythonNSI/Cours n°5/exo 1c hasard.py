from random import randint

nbdes = 1
des2 = 0
des10 = 10

while nbdes < 1001:
    nbdes = nbdes + 1
    x = randint(1, 10)
    if x == 2:
        des2 = des2 + 1
    elif x == 10:
        des10 = des10 + 1

pourcetage2 = (des2 / nbdes) * 100
pourcetage10 = (des10 / nbdes) * 100

print("Il y a", des2, "dés affichant 2 et", des10, "dés affichant 12")
print(pourcetage2, pourcetage10)