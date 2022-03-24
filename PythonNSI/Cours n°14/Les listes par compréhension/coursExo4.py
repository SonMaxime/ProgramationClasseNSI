from random import randint
liste = [randint(0,11) for i in range(0, 10000)]

liste2 = [liste for i in range(0, 10000) if liste[i] != 0]
print(liste2)