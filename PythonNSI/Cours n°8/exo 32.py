from random import randint

score = 0

for i in range(5):
    nb1 = randint(1, 20)
    nb2 = randint(1, 20)
    print("Nous avons de dès 1:",nb1, "et le dès 2:", nb2)
    resultat = nb1 * nb2
    x = int(input("Nombre ? "))

    if x == resultat:
        score+=+1
        print("Gagné")
    elif x != resultat:
        score = score - 1
        print("Perdu")

print("Vous avez", score, "points.")