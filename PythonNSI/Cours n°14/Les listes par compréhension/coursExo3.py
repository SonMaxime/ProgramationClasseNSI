# Les triples des nombres entre 1 et 1000 mais pairs

liste_triple = [3 * i for i in range(1, 1001) if 3 * i % 2 != 0]
print(liste_triple)