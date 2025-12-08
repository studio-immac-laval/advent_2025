import pyxel
from random import randint
from math import sqrt

pyxel.init(128, 128)

# Chargement du pyxres
pyxel.load('../advent.pyxres')

# Placement de Santa et du coucou
santaX = randint(10, 90)
santaY = randint(20, 90)
coucouX = (santaX + 12) if santaX < 48 else (santaX - 7)
coucouY = santaY - 8

def update() :
    pass

def draw() :
    global santaX, santaY, coucouX, coucouY
    
    # On dessine d'abord le fond
    pyxel.cls(9)
    
    # On dessine ensuite Santa
    pyxel.blt(santaX, santaY, 0, 0, 0, 32, 32, 3)

    # On dessine ensuite le coucou...
    pyxel.text(coucouX, coucouY, "coucou", 7)
    # ...avec une petite ligne dans le bon sens
    if coucouX < santaX :
        pyxel.line(coucouX + 12, coucouY + 6, coucouX + 13, coucouY + 7, 7)
    else :
        pyxel.line(coucouX + 11, coucouY + 6, coucouX + 10, coucouY + 7, 7)

    # Finalement on colorie toute l'image en noir sauf la zone à une distance de 16 pixels ou moins de la souris
    for i in range(128) :
        for j in range(128) :
            if sqrt((i - pyxel.mouse_x)**2 + (j - pyxel.mouse_y)**2) >= 16 :
                pyxel.pset(i, j, 0)

pyxel.run(update, draw)