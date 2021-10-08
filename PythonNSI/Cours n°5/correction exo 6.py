n = 0 # NB de notes
note = 0 # pour démarrer la boucle

somme = 0
moyenne = 0

while note != -1:
    note = float(input("Rentrez votre note: "))
    somme = somme + note
    n = n + 1
# Calcul de la moyenne
moyenne = somme / n
print("La moyenne vaut", moyenne)