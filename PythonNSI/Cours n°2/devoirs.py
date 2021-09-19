poids = float(input("Poids ? ")) # On demande le poids.
taille = float(input("Taille ? ")) # On demande la taille

imc = poids / taille**2 # On divise le poids par la taille qui a été "converti" au carré.
imc = round(imc, 1) # On arrondis le résultat à 1 chiffre après la virgule.

if 18.5 < imc < 25: #Si l'IMC se trouve entre 18,5 et 25
    print("Votre IMC est de", imc, ", tout est bon pour vous.") # Alors tout vas bien.
elif imc > 25: #Si l'IMC se trouve au dessus de 25
    print("Votre IMC est de", imc, ", attention, vous êtes au dessus de la normalité.")
elif imc < 18.5: #Si l'IMC se trouve en dessous de 18,5
    print("Votre IMC est de", imc, ", attention, vous êtes en dessous de la normalité...")