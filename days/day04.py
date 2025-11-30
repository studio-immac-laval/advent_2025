import pyxel

pyxel.init(128, 128)

steps = 0

def update() :
    global steps
    steps += 1 

def draw() :
    global steps
    pyxel.cls(4)

    # Ligne par ligne
    for y in range(21) :

        # Caractère par caractère
        for x in range(33) :

            pyxel.text(
                -4 + x * 4 + ((-1 * steps % 5) if y % 2 == 0 else (steps % 5)), # Une ligne sur deux on recule/avance de 0 à 4 pixels à chaque étape
                 1 + y * 6, 
                 str(y % 10), 
                 7
            )

pyxel.run(update, draw)