import time
from random import randint

print("bienvenue sur la machine à sous")
liste_fruits=["ananas", "cerise","orange","pasteque","pomme"]
    
fruits_sortis=[]    # création de la la liste des 3 fruits sortis
for i in range(3):  # on tire au sort 3fois un nombres compris entre 1 et 100 
    hasard=randint(1,100)
    if hasard <=40:               # tirage d'ananas 40% de chance
        symbole=liste_fruits[0]     
    elif hasard >40 and hasard<=65:
        symbole=liste_fruits[1]     # tirage de cerise
    elif hasard >65 and hasard<=85:
        symbole=liste_fruits[2]     # tirage d'orange
    elif hasard>85 and hasard <=95:
        symbole=liste_fruits[3]     # tirage de pastèque
    elif hasard >95:
        symbole=liste_fruits[4]   # tirage de pomme
    
    fruits_sortis=fruits_sortis+[symbole]

print(fruits_sortis)

