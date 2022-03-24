from random import randint
noms = ["Robin Dubois", "Gragamel Lupin", "Alice Voldemort"]

with open('notes.txt', 'w') as file:
    for item in noms:
        rand = randint(0, 20)
        rand1 = randint(0, 20)
        rand2 = randint(0, 20)
        ligne = item + " " + str(rand) + " " + str(rand1) + " " + str(rand2)
        file.write("%s\n" % ligne)
file = open('notes.txt', 'r')
print(file.read())