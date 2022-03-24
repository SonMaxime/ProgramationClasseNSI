# lecture du fichier de données csv et enregistrement dans une liste
import csv
tab_poke=[]
with open('pokemon2.csv', 'r') as fichier:
    objet = csv.reader(fichier)
    for ligne in objet:
        tab_poke.append(ligne)
# nous utiliserons maintenant le tableau qui se nomme tab_poke
# -----------------------------------------------------------
# Afficher tout le tableau
print(tab_poke)
# Afficher la première ligne du tableau (légende)
print(tab_poke[0])
# Afficher le premier pokemon et ses caractéristiques
print(tab_poke[1])
# Afficher le pokemon Charizard et ses caractéristiques
for i in range(len(tab_poke)):
    if tab_poke[i][1]=="Charizard":
        print(tab_poke[i])
# Afficher le type1 de Bulbasaur
for i in range(len(tab_poke)):
    if tab_poke[i][1]=="Bulbasaur":
        print(tab_poke[i])
# chercher si le pokémon Axew est présent dans le tableau
for i in range(len(tab_poke)):
    if tab_poke[i][1]=="Axew":
        print("Le pokemon est présent dans la liste.")