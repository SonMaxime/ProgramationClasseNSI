from random import *
sommeDeBase = 10

nbDes1 = 0
lancés = 0
nbDes2 = 0

while sommeDeBase >=2:
    lancés = lancés + 1
    sommeDeBase = sommeDeBase - 2
    d1 = randint(1, 6)
    d2 = randint(1, 6)
    if d1 == d2:
        sommeDeBase = sommeDeBase + 4
        print(d1, " ", d2, " ", "vous avez gagné !")
    else:
        sommeDeBase = sommeDeBase
        print(d1, " ", d2, " ", "vous avez perdu...")
    
    if sommeDeBase >= 100:
        print("Vous avez fait", lancés, "lancés")
        break