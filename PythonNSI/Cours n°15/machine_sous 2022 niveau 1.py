import time
from random import randint
#niveau 1
print("bienvenue sur la machine à sous")

liste_fruits=["ananas", "cerise","orange","pasteque","pomme"]

for i in range(3):   # on choisit 3 symboles
    x=randint(0,4)   # on choisit les indices des fruits entre 0 et 4
    print(liste_fruits[x],end=" ")   # on affiche l'élément d'indice x de la liste de fruits
    time.sleep(1)     # temporisation de 1s

