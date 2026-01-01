# Jour 22

![Défi](../img/day22.gif)

## Défi

Créons un jeu de [Chrome Dino](https://en.wikipedia.org/wiki/Dinosaur_Game) avec Rudolf ! (2/3)

## Démarrer

**Deuxième partie** 

En utilisant les techniques vues précédemment, coder :

+   les traces de pas laissées par Rudolf dans la neige

+   le saut de Rudolf quand on appuie sur [Espace]

## Une solution

🐍 [Voir le fichier](day22.py)

```py
import pyxel
from random import randint

pyxel.init(128, 64)
pyxel.load('../advent.pyxres')

score = 0
start = False
delay = 0
obstacles = []
jumping = False
jumpStep = 0
rudolfY = 39

# Etoiles
stars = []
for i in range(9, 127, 10) :
    stars.append([i, randint(1, 55)])

# Traces
footprints = [5]

def frame_count() :
    return pyxel.frame_count - delay

def update() :
    global score, start, obstacles, stars, rudolfY, jumping, jumpStep, delay

    # Saut
    if frame_count() % 3 == 0 :
        if start and not jumping and pyxel.btn(pyxel.KEY_SPACE) :
            jumping = True
            jumpStep = -8
        if jumping :
            jumpStep += 1
            rudolfY += jumpStep
        if jumpStep == 7 :
            jumping = False
            jumpStep = 0

    # Traces
    if start :
        if len(footprints) > 0 and footprints[0] == -4:
            footprints.pop(0)
        for i in range(len(footprints)) :
            footprints[i] -= 1

    # Score et traces
    if start and frame_count() % 10 == 0 :
        score += 1
        if not jumping :
            footprints.append(5)
    elif start and frame_count() % 10 == 5 and not jumping :
        footprints.append(15)

    # Démarrage
    if not start and pyxel.btn(pyxel.KEY_SPACE) :
        start = True
        delay = frame_count()

    # Etoiles
    if start :
        if stars[0][0] == 0:
            stars.pop(0)
            stars.append([127, randint(1, 55)])
        for i in range(len(stars)) :
            stars[i][0] -= 1

def draw() :
    global score, start, obstacles, rudolfY
    pyxel.cls(1)
    
    # Sol
    pyxel.line(0, 57, 128, 57, 0)
    pyxel.rect(0, 58, 128, 6, 7)

    # Traces
    for x in footprints :
        pyxel.line(x, 59, x + 2, 59, 13)

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
        if frame_count() % 10 < 5 :
            pyxel.blt(5, rudolfY, 0, 32, 0, 21, 21, 10)
        else :
            pyxel.blt(5, rudolfY, 0, 48, 24, 21, 21, 10)
    else :
        pyxel.blt(5, 39, 0, 32, 0, 21, 21, 10)

pyxel.run(update, draw)
```