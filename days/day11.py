import pyxel

pyxel.init(128, 128)
pyxel.load("../advent.pyxres")

buttons = 0
konami  = [pyxel.KEY_UP, pyxel.KEY_UP, pyxel.KEY_DOWN, pyxel.KEY_DOWN, pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_LEFT, pyxel.KEY_RIGHT, pyxel.KEY_A, pyxel.KEY_B, pyxel.KEY_RETURN]
switch = True

def update() :
    global buttons, konami, switch

    # Validation des boutons dans l'ordre
    if buttons < len(konami) and pyxel.btnp(konami[buttons]) :
        buttons += 1

    # Même si on n'annule pas la séquence en cas d'erreur... 🤫

    # Clignotement du tréma
    if pyxel.frame_count % 15 == 0 :
        switch = not switch

def draw() :
    global buttons, konami, switch
    pyxel.cls(0)
    
    # Affichage de la séquence
    x = 4
    for i in range(buttons) :
        if konami[i] == pyxel.KEY_UP :
            pyxel.blt(x, 31, 0, 0, 32, 7, 7, rotate = 0)
            x += 9
        elif konami[i] == pyxel.KEY_LEFT :
            pyxel.blt(x, 31, 0, 0, 32, 7, 7, rotate = 270)
            x += 9
        elif konami[i] == pyxel.KEY_DOWN :
            pyxel.blt(x, 31, 0, 0, 32, 7, 7, rotate = 180)
            x += 9
        elif konami[i] == pyxel.KEY_RIGHT :
            pyxel.blt(x, 31, 0, 0, 32, 7, 7, rotate = 90)
            x += 9
        elif konami[i] == pyxel.KEY_A :
            pyxel.blt(x, 30, 0, 8, 32, 8, 8)
            pyxel.blt(x + 4, 39, 0, 5, 40, 4, 5)
            x += 10
        elif konami[i] == pyxel.KEY_B :
            pyxel.blt(x, 30, 0, 8, 32, 8, 8)
            pyxel.blt(x + 4, 39, 0, 0, 40, 4, 5)
            x += 10
        elif konami[i] == pyxel.KEY_RETURN :
            pyxel.blt(x, 30, 0, 16, 32, 28, 14)
            x += 28
    
    # Affichage du Joyeux Noël
    if buttons == len(konami) :
        pyxel.text(40, 60, "Joyeux Noel !", 7)
        pyxel.pset(76, 59, 8 if switch else 11)
        pyxel.pset(78, 59, 11 if switch else 8)

pyxel.run(update, draw)