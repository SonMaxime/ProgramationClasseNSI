prim = int(input("Combien de potds de primevères avez-vous acheteés ? "))
camp = int(input("Combien de potds de camp avez-vous acheteés ? "))

apayer = prim * 1.80 + camp * 2.40

if prim >= 6 and camp >= 5:
    reduction = round(apayer * 0.1, 2)
    apayer = round(apayer - reduction, 2)
    print("Montant à payer:", apayer, "euros")
    print("Reduction:", reduction)
else:
    print("Montant à payer:", apayer, "euros")
    print("Pas de réduction")