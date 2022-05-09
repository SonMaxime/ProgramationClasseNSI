from this import d


dVilles = {
    'Nice' : 350000, 
    'Aix-en-Provence' : 140000, 
    'Marseille' : 850000, 
    'Caen' : 110000, 
    'Dijon' : 150000, 
    'Besançon' : 120000, 
    'Brest' : 140000, 
    'Nîmes' : 140000,
    'Toulouse' : 440000, 
    'Bordeaux' : 240000, 
    'Montpellier' : 250000, 
    'Rennes' : 210000,
    'Tours' : 140000, 
    'Grenoble' : 160000, 
    'Saint-Étienne' : 170000, 
    'Nantes' : 280000,
    'Orléans' : 110000, 
    'Angers' : 150000, 
    'Reims' : 180000, 
    'Nancy' : 110000, 
    'Metz' : 120000, 
    'Lille' : 230000, 
    'Clermont-Ferrand' : 140000, 
    'Perpignan' : 120000,
    'Strasbourg' : 270000, 
    'Mulhouse' : 110000, 
    'Lyon' : 480000, 
    'Villeurbanne' : 140000, 
    'LeMans' : 140000, 
    'Rouen' : 110000, 
    'Le Havre' : 180000, 
    'Amiens' : 130000, 
    'Toulon' : 170000, 
    'Limoges' : 140000, 
    'Boulogne-Billancourt' : 110000, 
    'Montreuil' : 100000,
    'Saint-Denis' : 100000, 
    'Argenteuil' : 100000, 
    'Saint-Denis' : 150000, 
    'Saint-Paul' : 100000
}
dVilles["Paris"] = 2200000
if "Paris" in dVilles:
    print("Oui, Paris est bien là, dommange")
else:
    print("Paris n'es pas là, encore heureux")
print(len(dVilles))
print(dVilles.keys())
print(sorted(dVilles))
dVillesSorted = {}
for i in dVilles.values():
    if 200000 < dVilles[i][1] < 500000:
        dVillesSorted[dVilles[i]] = dVilles[1]