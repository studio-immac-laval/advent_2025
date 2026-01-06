# Jour 21

![Défi](../img/day21.gif)

## Défi

Créons un jeu de [Chrome Dino](https://en.wikipedia.org/wiki/Dinosaur_Game) avec Rudolf ! (1/4)

## Démarrer

**Première partie** 

En utilisant les techniques vues précédemment, coder :

+ Un ciel et un sol fixe,

+ Rudolf qui gambade sans avancer,

+ Un ciel étoilé qui avance,

+ Un score qui s'incrémente régulièrement mais pas trop vite,

+ Une partie qui se lance quand on appuie sur espace.

## Une solution

🐍 [Voir le fichier](day21.py)

```py
import pyxel
from random import randint

pyxel.init(128, 64)
pyxel.load('../advent.pyxres')

score = 0
start = False
obstacles = []

# Etoiles
stars = []
for i in range(9, 128, 10) :
    stars.append([i, randint(10, 50)])

def update() :
    global score, start, obstacles, stars

    # Score
    if start and pyxel.frame_count % 10 == 0 :
        score += 1
        stars.pop(0)
        stars.append([127, randint(10, 50)])

    # Démarrage
    if not start and pyxel.btn(pyxel.KEY_SPACE) :
        start = True

    # Etoiles
    if start :
        for i in range(len(stars)) :
            stars[i][0] -= 1

def draw() :
    global score, start, obstacles
    pyxel.cls(1)
    
    # Sol
    pyxel.line(0, 57, 128, 57, 0)
    pyxel.rect(0, 58, 128, 6, 7)

    # Etoiles
    for [x, y] in stars :
        pyxel.pset(x, y, 7)

    # Score
    pyxel.text(103, 3, str(score).rjust(5, "0"), 7)

    # Message de lancement
    if not start :
        pyxel.rect(10, 29, 105, 6, 1)
        pyxel.text(11, 30, "- Press [space] to start -", 7)
    
    # Rudolf
    if start :
        if pyxel.frame_count % 10 < 5 :
            pyxel.blt(5, 39, 0, 32, 0, 21, 21, 10)
        else :
            pyxel.blt(5, 39, 0, 48, 24, 21, 21, 10)
    else :
        pyxel.blt(5, 39, 0, 32, 0, 21, 21, 10)

pyxel.run(update, draw)
```