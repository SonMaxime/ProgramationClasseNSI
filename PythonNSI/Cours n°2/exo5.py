prix = int(input("Quel est le prix de cet article ? ")) # On demande le prix de l'article

solde = int(input("Quel est le pourcentage de reduction ? ")) # On demande son pourcentage de reduction
solde = solde / 100 # On divise la reduction par 100 pour convertir en décimal.

prixfinal = prix * solde # On divise le prix de l'article en le multipliant par la réduction qu'on a divisé

print("Le prix final est de", prixfinal) # On donne le prix final après réduction.