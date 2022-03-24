from time import time
liste = [150, 30, 67, 4, 76, 98, 96]
n = len(liste)
debut = time()
for i in range(0, n-1):
    indice_min = i
    for j in range (i + 1, n): # Boucle qui parcourt le reste de la liste
        if liste[j] < liste[indice_min]:
            indice_min = j
    if indice_min != i:
        #Permutation
        temp = liste[indice_min]
        liste[indice_min] = liste[i]
        liste[i] = temp

print(liste)
print("Le temps vaut", time() - debut)