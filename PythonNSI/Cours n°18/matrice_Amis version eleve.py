# "Etre ami" avec quelqu'un
from operator import index


noms=["alice","bob","chloé","david","emma","fred","zoé"]
friend = [[0, 1, 1, 0, 0, 0, 1],                      # matrice d'adjacence
          [0, 0, 0, 0, 1, 1, 0],
          [1, 0, 0, 1, 1, 1, 0],
          [1, 0, 1, 0, 0, 1, 0],
          [0, 1, 1, 0, 0, 1, 0],
          [0, 1, 1, 0, 1, 0, 0],
          [1, 0, 0, 1, 0, 0, 0]]

# "suivre" quelqu'un

follow = [[0, 0, 1, 0, 0, 0, 1],                      # matrice d'adjacence
        [0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 0, 1, 1],
        [1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 1, 1],
        [0, 0, 0, 0, 1, 0, 1],
        [0, 0, 0, 0, 0, 0, 0]]

# compter les amis d'alice
compteur = 0
for i in range(7):
    if friend[0][i] == 1:
        compteur += 1 
print(compteur)
# vérifier que emma (indice4) et bob (indice1) sont amis
if friend[4][1] == 1:
    print("Amis")
else: 
    print("Pas amis")
# entrer deux noms et trouver leur indice dans la liste de noms.
noms=["alice","bob","chloé","david","emma","fred","zoé"]
input1 = input("Entrez un nom: ")
input2 = input("Entrez un 2nd nom: ")
index1 = noms.index(input1)
index2 = noms.index(input2)
# chercher alors si ils sont amis.
if friend[index1][index2] == 1:
    print("Amis")
else:
    print("Pas amis")