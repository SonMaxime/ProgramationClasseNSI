from time import sleep

quantitéInitiale = 350

while quantitéInitiale >= 0:
    jours = 0
    quantitéInitiale = quantitéInitiale - 27
    print("Vous avez vendu 27 articles, vous êtes à", quantitéInitiale)
    sleep(3)
