seuil = 0
temp = [10, 9, 8, 7, 6, 5, 4, 5, 8, 11, 15, 18]
horaires = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

while temp[seuil] < 11:
    print(horaires[seuil], "H: ", temp[seuil], "°")
    seuil =+ 1