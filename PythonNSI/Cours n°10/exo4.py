from random import randint

nb6= 0
n = int(input("Combien de fois voulez vous lancer les 2 dès ? "))

for i in range (n):
    des1 = randint(1, 6)
    des2 = randint(1, 6)
    if des1 + des2 == 6:
        nb6 += 1
frequence = nb6 / n * 100

print("Vous avez eu la fréquence", round(frequence, 1), "%")