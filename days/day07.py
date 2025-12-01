import pyxel
from random import randint

pyxel.init(128, 128)

# Chargement du pyxres
pyxel.load('../advent.pyxres')

# Initialisation de la position de départ de Rudolf
x = randint(20, 100)
y = randint(20, 100)

# Décalage à chaque étape pour x et y
dx = randint(-20, 20) / 10
dy = randint(-20, 20) / 10

def update() :
    global x, y, dx, dy
    
    # Décalage de x
    x += dx

    # Gestion des collisions avec les bords gauche et droite
    if x < 0 or x > 109 :
        x -= dx
        dx = -dx

    # Décalage de y
    y += dy

    # Gestion des collisions avec les bords haut et bas
    if y < 0 or y > 107 :
        y -= dy
        dy = -dy


def draw() :
    global steps
    pyxel.cls(7)
    
    # On dessine Rudolf
    pyxel.blt(x, y, 0, 32, 0, 21 * (-1 if dx < 0 else 1), 21, 10, )
                                   #^^^^^^^^^^^^^^^^^^^ Pour l'afficher dans le bon sens !

pyxel.run(update, draw)