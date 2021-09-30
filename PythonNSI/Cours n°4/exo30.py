# juste prix

i = 1
justeprix = 30000

while(i < 5):
    nombre = int(input("Prix de cet objet ? "))
    if nombre == justeprix:
        print("Bravo.")
        break
    else:
        if i == 4:
            print("Vous avez perdu.")
            break
        else:
            print("Réassayez.")
            i = i + 1