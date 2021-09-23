temp = int(input("Température ? "))

if temp <= 0:
    print("Etat: Solide")
elif temp > 0 & temp < 100:
    print("Etat: Liquide")
elif temp >= 100:
    print("Etat: Gazeux")