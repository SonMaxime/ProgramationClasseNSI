quantite = input("Carnet ou ticket unité ? ") # On demande la quantité
categorie = input("Catégorie d'achat ? ") # On demande la catégorie

if quantite == "Unité":
    if categorie == "Scolaire": # Si on choisi un ticket dans la catégorie Scolaire
        print("Vous devez payer 1,20$")
    elif categorie == "Handicape": # Si on choisi un ticket dans la catégorie Handiacpe
        print("Vous devez payer 0,50$")
    elif categorie == "Précaire": # Si on choisi un ticket dans la catégorie Précraire
        print("Vous devez payer 0,70$")
    elif categorie == "Normal": # Si on choisi un ticket dans la catégorie Normal
        print("Vous devez payer 1,50$")
elif quantite == "Carnet":
    if categorie == "Scolaire": # Si on choisi un carnet dans la catégorie Scolaire
        print("Vous devez payer 5$")
    elif categorie == "Handicape": # Si on choisi un carnet dans la catégorie Handicape
        print("Vous devez payer 2,10$")
    elif categorie == "Précaire": # Si on choisi un carnet dans la catégorie Précraire
        print("Vous devez payer 2,50$")
    elif categorie == "Normal": # Si on choisi un carnet dans la catégorie Normal
        print("Vous devez payer 7$")