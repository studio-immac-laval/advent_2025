import pyxel

pyxel.init(128, 128)

DIRECTION_NORTH = 0
DIRECTION_EAST = 1
DIRECTION_SOUTH = 2
DIRECTION_WEST = 3

# Création du serpent
snake = {
    "x" : 64,
    "y" : 64,
    "length" : 5,
    "direction" : DIRECTION_NORTH,
    "previous" : [[64, 64]]
}

def update() :
    global snake
    
    # Sauvegarde "sommaire" de la position
    snake["previous"].append([snake["x"], snake["y"]])
    if len(snake["previous"]) > snake["length"] * 8 :
        snake["previous"].pop(0)

    # Changement de direction (mais pas de demi-tour !)
    if (pyxel.frame_count) % 8 == 0 :
        if snake["direction"] != DIRECTION_SOUTH and pyxel.btn(pyxel.KEY_UP) :
            snake["direction"] = DIRECTION_NORTH
        elif snake["direction"] != DIRECTION_NORTH and pyxel.btn(pyxel.KEY_DOWN) :
            snake["direction"] = DIRECTION_SOUTH
        elif snake["direction"] != DIRECTION_EAST and pyxel.btn(pyxel.KEY_LEFT) :
            snake["direction"] = DIRECTION_WEST
        elif snake["direction"] != DIRECTION_WEST and pyxel.btn(pyxel.KEY_RIGHT) :
            snake["direction"] = DIRECTION_EAST

    # Avancée inexorable
    if snake["direction"] == DIRECTION_EAST :
        snake["x"] += 1
    elif snake["direction"] == DIRECTION_WEST :
        snake["x"] -= 1
    elif snake["direction"] == DIRECTION_NORTH :
        snake["y"] -= 1
    elif snake["direction"] == DIRECTION_SOUTH :
        snake["y"] += 1

    # Gestion des bords de l'écran
    if snake["x"] == -4 :
        snake["x"] = 124
    elif snake["x"] == 124 :
        snake["x"] = -4
    elif snake["y"] == -4 :
        snake["y"] = 124
    elif snake["y"] == 124 :
        snake["y"] = -4

def draw() :
    global snake
    pyxel.cls(0)
    
    # Affichage du serpent
    for i in range(len(snake["previous"])) :
        pyxel.rect(snake["previous"][i][0], snake["previous"][i][1], 8, 8, 9)

pyxel.run(update, draw)