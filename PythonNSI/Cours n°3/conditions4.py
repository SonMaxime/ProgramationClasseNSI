from math import sqrt

a = int(input("Valeur de a ? "))
b = int(input("Valeur de b ? "))
c = int(input("Valeur de c ? "))

delta = b**2 - (4 * a * c)


if delta > 0:
    xprime = (-b + sqrt(delta)) / (2*a)
    xprime2 = (-b - sqrt(delta)) / (2*a)
    print("Les solutions sont", xprime, "et", xprime2)
elif delta == 0:
    xprime2 = -b / 2*a
    print("La solution est", xprime2)
elif delta < 0:
    print(".")