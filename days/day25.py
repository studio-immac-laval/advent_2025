import pyxel
from random import randint
from math import sin

pyxel.init(128, 128)

font = pyxel.Font("..\\fonts\\4x6.bdf")

steps = 0
message = "Joyeux Noël !!!"
stars = []

def update() :
    global steps

    if pyxel.frame_count % 50 > 40 :
        steps += 1
    else :
        steps = 0

    for i in range(len(stars)) :
        stars[i][0] += stars[i][2]
        stars[i][1] += stars[i][3]

    stars.append([64, 64, randint(-7,7), randint(-7,7)])
    
    if len(stars) > 100 : 
        stars.pop(0)

def draw() :
    global steps, message
    pyxel.cls(1)

    for star in stars :
        pyxel.pset(star[0], star[1], 7)

    pyxel.circ(64, 64, 5, 1)
    
    for i in range(len(message)) :
        if steps != 0 :
            pyxel.text(34 + i * 4, 61 + sin(i + steps), message[i], i if i < 1 else i + 1, font)
        else :
            pyxel.text(34 + i * 4, 61, message[i], i if i < 1 else i + 1, font)
    

pyxel.run(update, draw)