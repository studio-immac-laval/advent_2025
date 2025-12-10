import pyxel

pyxel.init(128, 128)
pyxel.mouse(True)

previous = []

def update() :
    global previous

    # On enregistre les positions précédentes si on clique
    if pyxel.btn(pyxel.MOUSE_BUTTON_LEFT) :
        previous.append([pyxel.mouse_x, pyxel.mouse_y])
    # Onn efface quand on relâche
    elif len(previous) > 0 :
        previous.pop(0)
    
def draw() :
    global previous
    pyxel.cls(12)

    color = 1
    
    if len(previous) > 2 :
        # On affiche les précédentes positions reliées par une ligne
        for i in range(len(previous) - 1) :
            pyxel.line(previous[i][0], previous[i][1], previous[i + 1][0], previous[i + 1][1], 8)
            # On change de couleur toutes les 10 positions
            if i % 10 == 0 :
                color += 1 if color == 7 else 2

pyxel.run(update, draw)