anneenaissance = int(input("Quel année de naissance ? "))
anneeactuelle = int(input("Année actuelle ? "))

calculannee = anneeactuelle - anneenaissance

if calculannee < 18:
    print("Vous avez:", calculannee, "an(s), vous êtes mineur.")
elif calculannee >= 18:
    print("Vous avez", calculannee, "an(s), vous êtes majeur.")