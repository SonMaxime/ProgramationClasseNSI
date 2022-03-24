liste = [48, 17, 25, 9, 34]
n = len(liste) #Nombre d'éléments
for i in range(0, n - 1): #Je parcours toute la liste
    for j in range(i, n - 1):
        if liste[j] < liste[i]:
            #permutation