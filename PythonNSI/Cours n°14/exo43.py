liste = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pière', 'Sandra'] # Liste originelle
liste1 = [] # Petits prénoms
liste2 = [] # Grands prénoms de 6 ou plus caractères

for prénom in liste: # Prénom prends tous les éléments de la liste
    if len(prénom) < 6: # Si prénom en dessous de 6 lettres
        liste1.append(prénom) # Ajouter le prénom à la liste 1
    elif len(prénom) >= 6: # Si prénom de 6(+) lettres
        liste2.append(prénom) # Ajouter le prénom à la liste 2

print(liste1)
print(liste2)
