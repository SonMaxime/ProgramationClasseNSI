from math import pi
from random import randint

piece = 1
pile = 0
face = 0

while piece < 101:
    piece = piece + 1
    x = randint(1, 2)
    while pile < 4:
        if x == 1:
            pile = pile + 1
        elif x == 2:
            face = face + 1

    if pile == 4:
        print(pile)
        break