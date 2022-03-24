noms=["alice","bob","chloé","david","emma","fred","zoé"]
input1 = input("Entrez un nom: ")
input2 = input("Entrez un 2nd nom: ")
for i in range(len(noms) + 1):
    if input1 == noms[i]:
        print(input1, "est présent(e) dans la liste, il/elle est d'indice", i)
        break
for y in range(len(noms) + 1):
    if input2 == noms[y]:
        print(input2, "est présent(e) dans la liste, il/elle est d'indice", y)
        break