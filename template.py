import pyxel

pyxel.init(128, 128)

steps = 0

def update() :
    global steps
    steps += 1 

def draw() :
    global steps
    pyxel.cls(0)
    
    pyxel.text(10, 10, str(steps), 7)

pyxel.run(update, draw)