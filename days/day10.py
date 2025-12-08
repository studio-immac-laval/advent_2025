import pyxel

pyxel.init(128, 128)

square = 0
speed = 1

def update() :
    global square, speed
    #if pyxel.frame_count % 2 == 0 :
    if square < 112 :
        square += speed
        speed += 1
        if square > 112 :
            square = 112
    

def draw() :
    global steps
    pyxel.cls(0)
    
    pyxel.rect(60, square, 8, 8, 9)
    pyxel.line(0, 120, 127, 120, 8)

pyxel.run(update, draw)