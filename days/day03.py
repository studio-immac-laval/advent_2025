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