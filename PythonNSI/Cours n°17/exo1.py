t = [[2, -5, 3], [7, 4, -1]]
print(t[1][2])
print(t[0][0])
somme = 0
for col in range(3):
    somme += t[0][col]

print("La somme de la 1ere ligne est", somme)