from random import randint

x = randint(10, 20)

biere = 5 # Prix bière
vin = 12 # Prix vin
coctail = 14 # Prix coctail
taxe = 0

totalbiere = int(input("Combien de bières souhaitez vous ? ")) # On demande le nombre de bières 
totalvin = int(input("Combien de vins souhaitez vous ? ")) # On demande le nombre de vins
totalcoctail = int(input("Combien de coctail souhaitez vous ?")) # On demande le nombre de coctails 

# Addition de la somme des prix pour en donner le prix final
prixtotal = (biere * totalbiere) + (vin * totalvin) + (coctail + totalcoctail) 

if x <= 8:
    taxe = prixtotal + ((prixtotal * 0.88) - prixtotal)
    prixtotal = prixtotal + taxe

if totalbiere == 2 & totalcoctail < 1:
    prixtotal = prixtotal - 3

if prixtotal < 50: # Si le prix est inférieur à 50
    print("Le prix total est de", prixtotal, "$ bonne journée.")
elif 50 < prixtotal < 100: # Si le prix est compris entre 50 et 100
    print("Le prix total est de", prixtotal, "$ merci beaucoup pour votre commande.")
elif prixtotal > 100: # Si le prix est suppérieur à 100
    print("Le prix total est de", prixtotal, "$ merci à notre client du jour.")
