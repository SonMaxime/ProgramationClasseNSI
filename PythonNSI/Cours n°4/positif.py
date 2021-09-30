n = int(input("Nombre ? "))

if n > 0:
    if n % 2 == 0:
        print("Le nombre est paire positif")
    else:
        print("Le nombre est impaire positif.")
else:
    print("Le nombre est négatif.")