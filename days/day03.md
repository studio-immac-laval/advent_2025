# Jour 3

![Défi](../img/day03.gif)

## Défi

Faire neiger des pixels et les entasser en bas de l'écran.

## Démarrer

Créer une liste de flocons puis l'alimenter à chaque `update()` avec un nombre de flocons aléatoirement placés sur la première ligne de l'écran.

Un flocon est représenté par ses coordonnées `x` et `y` dans une liste.

La liste des flocons est donc une liste de liste.

A chaque `update()`, on ajoute 1 à la coordonnées `y` de chaque flocon, ce qui a pour effet de les faire descendre.

Pour la solution ci-dessous, on a choisit d'arrêter la chute du flocon soit quand il atteint le bas de l'écran soit si le pixel juste au-dessous est blanc (i.e. le flocon précédent dans la colonne est arrêté !).

## Une solution

🐍 [Voir le fichier](day03.py)

```py
import pyxel
from random import randint

pyxel.init(128, 128)

snow = []

def update() :
    global snow

    # On descend tous les flocons
    for i in range(len(snow)) :
        if pyxel.pget(snow[i][0], snow[i][1] + 1) != 7 and snow[i][1] < 127 :
            snow[i][1] += 1
    
    # On limite le nombre de flocons à la moitié de l'écran
    if len(snow) < 128 * 64 :
        # Ajouter des 3 à 10 flocons
        for i in range(randint(3, 10)) :
            snow.append([randint(0, 127), 0])

def draw() :
    global steps
    pyxel.cls(3)

    # On affiche tous les flocons
    for i in range(len(snow)) :
        pyxel.pset(snow[i][0], snow[i][1], 7)
    

pyxel.run(update, draw)
```