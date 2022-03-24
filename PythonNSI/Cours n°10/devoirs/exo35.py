from random import randint
from math import sqrt

x = randint(1, 100)
y = randint(1, 100)

for i in range(1, 6):
    valeurX = int(input("Selon vous, quel est la valeur de x ? "))
    valeurY = int(input("Selon vous, quel est la valeur de y ? "))

    if valeurX and valeurY == x and y:
        print("Coup chanceux !")
    else:
        if valeurX < x:
            ecartX = x - valeurX
        elif valeurX > x:
            ecartX = valeurX - x
        
        if valeurY < y:
            ecartY = y - valeurY
        elif valeurY > y:
            ecartY = ecartY - y
        
        formuleDistance = ((x - ecartX)**2) + ((y - ecartY)**2)
        calcul = sqrt(formuleDistance)
        print("Dommage, l'écart était de", calcul, "cases.")