tarif1chambre = 120 #Prix d'une chambre
tarif1dejeuner = 10 #Prix d'un déjeuner

nombrechambres = int(input("Quel est le nombre de chambres désiré ? ")) #On demande le nombre de chambres souhaité

nombredejeuner = int(input("Quel est le nombre de déjeuners désiré ? ")) #One demande le nombre de déjeuner souhaité

prixtotal = (tarif1chambre * nombrechambres) + (tarif1dejeuner * nombredejeuner) # On calcule le prix total en multipliant le tarif chambre par le nombre de ce dernier souhaité auquel on ajoute le prix total des déjeuners.
prixavecreduc = prixtotal * 0.88 # 100 - 12 = 88 = 12 pourcents

print("Le prix total est de", prixtotal, "mais avec la réduction, le prix passe à", prixavecreduc) #On renvoie le prix total.