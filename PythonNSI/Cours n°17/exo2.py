tab = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
for i in range(len(tab)):
    print(tab[i][0])
print(tab[2])
for ligne in range(len(tab)):
    for colonne in range(4):
        print(tab[ligne][colonne], end=" ")