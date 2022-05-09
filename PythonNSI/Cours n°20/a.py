poids_max = 5.0
objets=[[2,1],[5,0.5],[1,0.2],[3,4]]
def remplir_sac(objets,poids_max):
    # créer une nouvelle liste objets_tries, triée par valeur décroissante et l'afficher (sorted)
    objets_tries = sorted(objets, reverse=True)
    n = len(objets)
    objets_choisi = [0 for i in range(n)]
    for y in range(n):
        if objets_tries[y][1] <= poids_max:
            objets_choisi[y] += 1
            poids_max -= objets_tries[y][1]
    print(objets_choisi)    
remplir_sac(objets, poids_max)