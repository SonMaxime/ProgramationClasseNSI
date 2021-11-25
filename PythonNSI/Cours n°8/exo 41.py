from random import randint

nombreDeFois50 = 0

for i in range(5000):
    x = randint(1, 99)
    print(x)
    if x == 50:
        nombreDeFois50 = nombreDeFois50 + 1

print("On a obtenu le nombre 50:", nombreDeFois50, "fois.")