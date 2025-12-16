import pyxel
from math import sqrt

pyxel.init(128, 128)
pyxel.load("../advent.pyxres")

steps = 0
direction = 1
moving = False

def update() :
    global moving, direction, steps
    
    # Le mouvement est piloté par la souris ou la touche espace
    if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT) or pyxel.btnp(pyxel.KEY_SPACE) :
        moving = not moving
        if not moving :
            direction = direction * -1

    if moving :
        steps += direction
        if (direction == 1 and steps == 120) or (direction == -1 and steps == 0) :
            moving = False 
            direction = direction * -1 

def draw() :
    global steps

    pyxel.cls(0)
    
    # Affichage du fond
    pyxel.blt(0, 0, 0, 0, 48, 128, 128)
    
    # affichage du titre
    pyxel.blt(0, steps / 2 - 40, 0, 0, 176, 128, 43, 7)

    # Montée/descente du rideau
    for i in range(0, 118, 16) :
        for j in range(120 - steps, -4 - steps, -4) :
            pyxel.blt(i, j, 0, 32, 24, 16, 8, 0)

pyxel.run(update, draw)