def calcul_pi(n):
    i = 0
    somme = 0
    while i < n:
        formule = ((-1)**i) / ((2*i) + 1)
        somme = somme + formule
        i = i + 1
    return somme * 4

print(calcul_pi(1000000000))