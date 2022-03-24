# Trouver les carrés des nombres entre 1 et 100 :
liste = []
for i in range(1, 101):
    carré = i ** 2
    liste.append(carré)

# 2ème méthode:

liste_carré = [i ** 2 for i in range(1, 101)]
print(liste_carré)