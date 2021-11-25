somme = int(input("Somme ? "))
nbannes = int(input("Pendant combien de temps souhaitez vous gagner vos interêts? "))

for i in range(1, nbannes + 1):
    somme = somme * 1.03

print("Vous avez", somme, "euros au bout de", nbannes, "ans d'interêts.")