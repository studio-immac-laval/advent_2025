# Jour 12

![Défi](../img/day12.gif)

## Défi

Dessiner à la souris une trace éphémère.

## Démarrer

Challenge assez simple, il faut conserver les n dernières positions de la souris avec `pyxel.mouse_x` et `pyxel.mouse_y` et les relier avec `pyxel.line()`.

## Une solution

🐍 [Voir le fichier](day12.py)

```py
import pyxel

pyxel.init(128, 128)

previous = []

def update() :
    global previous

    # On enregistre les positions précédentes
    previous.append([pyxel.mouse_x, pyxel.mouse_y])

    # On limite à 100
    if len(previous) > 100 :
        previous.pop(0)
    
def draw() :
    global previous
    pyxel.cls(0)

    color = 1
    
    if len(previous) > 2 :
        # On affiche les précédentes positions reliées par une ligne
        for i in range(len(previous) - 1) :
            pyxel.line(previous[i][0], previous[i][1], previous[i + 1][0], previous[i + 1][1], color)
            # On change de couleur toutes les 10 positions
            if i % 10 == 0 :
                color += 1 if color == 7 else 2

pyxel.run(update, draw)
```