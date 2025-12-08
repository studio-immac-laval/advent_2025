# Jour 7

![Défi](../img/day07.gif)

## Défi

Afficher un Rudolf qui se déplace en ligne droite et rebondit sur les murs.

## Démarrer

Petits conseils pour éviter de proposer toujours la même animation : 

+   La position initiale de Rudolf devrait être aléatoire.

+   L'"angle de départ" devrait aussi être aléatoire (entre 10 et 45).

## Une solution

🐍 [Voir le fichier](day07.py)

```py
import pyxel
from random import randint

pyxel.init(128, 128)

# Chargement du pyxres
pyxel.load('../advent.pyxres')

# Initialisation de la position de départ de Rudolf
x = randint(20, 100)
y = randint(20, 100)

# Décalage à chaque étape pour x et y = angle de déplacement
dx = randint(-20, 20) / 10
dy = randint(-20, 20) / 10

def update() :
    global x, y, dx, dy
    
    # Décalage de x
    x += dx

    # Gestion des collisions avec les bords gauche et droite, on repart dans l'autre sens
    if x < 0 or x > 109 :
        x -= dx
        dx = -dx

    # Décalage de y
    y += dy

    # Gestion des collisions avec les bords haut et bas, on repart dans l'autre sens
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
```