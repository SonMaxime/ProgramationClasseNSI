from time import sleep

def reduction(age):
    if age < 10:
        reduction = "Vous avez une réduction de 50%"
        return reduction
    elif 10 < age <= 18:
        reduction = "Vous avez une réduction de 30%"
        return reduction
    elif age > 60:
        reduction = "Vous avez une réduction de 20%"
        return reduction

def montant(tarif_normal, age):
    if age < 10:
        prixbillet = tarif_normal * 0.50
        return prixbillet
    elif 10 < age <= 18:
        prixbillet = tarif_normal * 0.70
        return prixbillet
    elif age > 60:
        prixbillet = tarif_normal * 0.80
        return prixbillet

age = int(input("Quel âge avez vous ? "))
tarif_normal = int(input("Quel est le prix de votre billet ? "))

print(reduction(age))
sleep(1)
print("Vous devez payer", montant(tarif_normal, age))