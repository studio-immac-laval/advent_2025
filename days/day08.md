# Jour 8

![Défi](../img/day08.gif)

## Défi

Cacher un Père Noël sous un fond noir et afficher un halo révélateur au survol de la souris.

## Démarrer

Ici tout se passe dans le `draw()`.

On constitue chaque image par couches : 

1.  On affiche le fond,

2.  On affiche le Père Noël,

3.  On colorie tout l'écran en noir sauf les pixels à une certaine distance (16 pixels dans l'exemple) du pointeur de la souris.

    Il faut utiliser les variables Pyxel liées à la souris et sa position : `pyxel.mouse_x` et `pyxel.mouse_y`.

    Comme Pyxel utilise un système de coordonnées, on peut utiliser la formule de la distance euclidienne pour calculer la distance entre deux points : 

    ![distance euclidienne](../img/euclidean_distance_2d.svg)
    
    *Distance euclidienne ([Wikipédia](https://fr.wikipedia.org/wiki/Distance_euclidienne))*

## Une solution

🐍 [Voir le fichier](day08.py)

```py
import pyxel
from random import randint
from math import sqrt

pyxel.init(128, 128)

# Chargement du pyxres
pyxel.load('../advent.pyxres')

# Placement du Père Noël et du coucou
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
    
    # On dessine ensuite le Père Noël
    pyxel.blt(santaX, santaY, 0, 0, 0, 32, 32, 3)

    # On dessine ensuite le coucou...
    pyxel.text(coucouX, coucouY, "coucou", 7)
    # ...avec une petite ligne dans le bon sens
    if coucouX < santaX :
        pyxel.line(coucouX + 12, coucouY + 6, coucouX + 13, coucouY + 7, 7)
    else :
        pyxel.line(coucouX + 11, coucouY + 6, coucouX + 10, coucouY + 7, 7)

    # Finalement on colorie toute l'image en noir (pixel par pixel) sauf la zone à une distance de 16 pixels ou moins de la souris
    for i in range(128) :
        for j in range(128) :
            if sqrt((i - pyxel.mouse_x)**2 + (j - pyxel.mouse_y)**2) >= 16 :
                pyxel.pset(i, j, 0)

pyxel.run(update, draw)
```