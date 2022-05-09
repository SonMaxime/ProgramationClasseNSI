pieces = [500,200,100,50,20,10,5,2,1]
somme = 1200

def rendu_monnaie(somme,pieces):
    piècesChoisies = [0 for i in range(len(pieces))]
    for i in range(len(pieces)):
        while somme >= pieces[i]:
            piècesChoisies[i] += 1
            somme -= pieces[i]
    print(piècesChoisies)
rendu_monnaie(somme, pieces)