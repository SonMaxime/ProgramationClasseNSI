année = int(input("En quel année avez vous planté votre sapin ? "))
taillearbre = float(input("Quel est la taille actuelle de votre sapin ? "))

while(taillearbre < 5):
    année = année + 1
    taillearbre = taillearbre + 0.30
print("Vous devez couper votre arbre en", année)