tab=[["denis",15], ["teddy",10],["james",8],["craig",16],["jason",5]]
# longueur du tableau
print(len(tab))
# afficher le nom et la moyenne de jason (on affiche sa ligne)
print(tab[4])
# afficher la moyenne de teddy
print(tab[1][1])
# afficher tous les prénoms
for i in range(len(tab)):
    print(tab[i][0],end=" ")
print()    
# chercher si craig est dans la liste et afficher alors sa moyenne
for i in range(len(tab)):
    if tab[i][0]=="craig":
        print("sa moyenne est ",tab[i][1])
