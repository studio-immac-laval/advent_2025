import pyxel
from random import randint
from math import sin

pyxel.init(128, 128)

# Chargement du pyxres
pyxel.load('../advent.pyxres')

steps = 0
stars = []

def update() :
    global steps, stars
    steps += 1
    
    # Déplacement des étoiles
    for i in range(len(stars)) :
        stars[i][0] -= 1

    # Ajout d'étoiles
    if steps % 2 == 0 :
        # Nettoyage
        if steps > 128 : 
            stars.pop(0)
        stars.append([127, randint(0, 127)])

def draw() :
    global steps, stars
    pyxel.cls(1)

    # Affichage des étoiles
    for i in range(len(stars)) :
        pyxel.pset(stars[i][0], stars[i][1], 7)

    # Arrivée de Rudolf
    if steps > 107 and steps < 128 + 54 :

        # Affichage de l'arc en ciel
        for i in range(steps - 128 + 3) :
            pyxel.pset(i, 67 + sin(steps + i), 8)
            pyxel.pset(i, 68 + sin(steps + i), 9)
            pyxel.pset(i, 69 + sin(steps + i), 10)
            pyxel.pset(i, 70 + sin(steps + i), 11)
            pyxel.pset(i, 71 + sin(steps + i), 12)
            pyxel.pset(i, 72 + sin(steps + i), 5)
        
        # Affichage de Rudolf
        pyxel.blt(steps - 128, 54 + sin(steps), 0, 32, 0, 21, 21, 10)
    
    # Position finale
    elif steps >= 128 + 54 :

        for i in range(58) :
            pyxel.pset(i, 67 + sin(steps + i), 8)
            pyxel.pset(i, 68 + sin(steps + i), 9)
            pyxel.pset(i, 69 + sin(steps + i), 10)
            pyxel.pset(i, 70 + sin(steps + i), 11)
            pyxel.pset(i, 71 + sin(steps + i), 12)
            pyxel.pset(i, 72 + sin(steps + i), 5)

        # Affichage de l'arc en ciel
        pyxel.blt(54, 54 + sin(steps), 0, 32, 0, 21, 21, 10)

pyxel.run(update, draw)