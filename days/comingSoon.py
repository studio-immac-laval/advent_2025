import pyxel
from math import sin

pyxel.init(128, 128)

steps = 0
message = "coming soon..."

def update() :
    global steps
    if pyxel.frame_count % 90 > 80 :
        steps += 1
    else :
        steps = 0

def draw() :
    global steps, message
    pyxel.cls(7)
    
    for i in range(len(message)) :
        if steps != 0 :
            pyxel.text(36 + i * 4, 61 + sin(i + steps), message[i], i + 1 if i <= 7 else i + 2)
        else :
            pyxel.text(36 + i * 4, 61, message[i], i + 1 if i <= 7 else i + 2)
    

pyxel.run(update, draw)