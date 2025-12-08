# Jour 5

![Défi](../img/day05.gif)

## Défi

Afficher un Père Noël et zoomer dessus en le faisant tourner.

## Démarrer

Pas de grosse difficulté, on apprend à utiliser le fichier de ressources et la fonction `pyxel.blt(x, y, img, u, v, w, h, [colkey], [rotate], [scale])` (et surtout les deux derniers paramètres 🤫).

## Une solution

🐍 [Voir le fichier](day05.py)

```py
import pyxel

pyxel.init(128, 128)

# Chargement du pyxres
pyxel.load('../advent.pyxres')

steps = 0
increasing = 1
scale = 0
rotation = 0

def update() :
    global steps, increasing, rotation, scale
    
    steps += 1
    
    # On augmente/diminue la taille toutes les 3 étapes 
    if steps % 3 == 0 :
        scale = scale + increasing
    
    # On change le sens (augmentation/diminution toutes les 200 étapes)
    if steps % 200 == 0 :
        increasing = - increasing
    
    # On tourne de 3° à chaque étape
    rotation = steps * 3

def draw() :
    global steps, rotation, scale
    pyxel.cls(5)
    
    # Affichage du Père Noël
    pyxel.blt(48, 48, 0, 0, 0, 32, 32, 3, rotate = rotation, scale = scale * 0.1)

pyxel.run(update, draw)
```