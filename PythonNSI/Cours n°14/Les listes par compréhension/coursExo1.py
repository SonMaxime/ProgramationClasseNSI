# 1)	Remplissons une liste avec 0, 1, 2, 3, 4 :

liste = []
for i in range(0, 5):
    liste.append(i)

print(liste)

# Ou méthode par compréhension:

liste1 = [i for i in range(5)]
print(liste1)