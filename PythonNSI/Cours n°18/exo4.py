from random import randint

tab = [[randint(1, 100) for i in range(8)] for a in range(8)] 
print(tab)

compteur_10 = 0
for ligne in range(8):
    for colonne in range(8):
        if tab[ligne][colonne] == 10:
            compteur_10 += 1

print(compteur_10)