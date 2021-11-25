somme = 0
n = int(input("Nombre d'étages ? "))

for i in range(1, n + 1):
    somme = somme + (i * i)

print("Il y a en tout", n, "étages et", somme,"billes")