# lecture du fichier de données csv et enregistrement dans une liste
import csv
from operator import index
tab_poke=[]
with open('pokemon.csv', 'r') as fichier:
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
print(list(filter(lambda a: 'Charizard' in a, tab_poke)))
# Afficher le type1 de Bulbazor

# chercher si le pokémon Axew est présent dans le tableau

