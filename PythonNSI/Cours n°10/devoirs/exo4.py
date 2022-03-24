n = int(input("Entrez la valeur de n: "))

def nombreDiviseurs(n):
    for i in range(1, n + 1):
        if n % i == 0:
            print(i, end=" ")

nombreDiviseurs(n)