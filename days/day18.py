import pyxel
from random import randint

pyxel.init(128, 128)

# Liste des niveaux

# Chaque niveau est décrit par :
# + size : la taille de son plateau (size * 8 pixels)
# + grid : La grille avec le chemin prévu (orientation cardinale : N, E, S et W)
# + start : Sa case de départ
# + end : La case d'arrivée

levels = [
    {
        "size" : 4,
        "grid" : [
            "XNXN",
            "XWNX",
            "XSXX",
            "SXEX",
        ],
        "start" : [0, 0],
        "end" : [3, 2]
    },
    {
        "size" : 4,
        "grid" : [
            "NEXN",
            "XSXE",
            "WXXX",
            "XXSX",
        ],
        "start" : [1, 2],
        "end" : [3, 3]
    },
    {
        "size" : 5,
        "grid" : [
            "NENEX",
            "XXWSE",
            "XXWSX",
            "XSXWX",
            "WXXSX",
        ],
        "start" : [3, 3],
        "end" : [4, 2]
    },
    {
        "size" : 5,
        "grid" : [
            "XENXX",
            "XXENN",
            "XXXXX",
            "XXWSX",
            "SXXXE",
        ],
        "start" : [0, 0],
        "end" : [3, 0]
    },
    {
        "size" : 6,
        "grid" : [
            "XXXWXN",
            "XXXXXX",
            "WXSXXX",
            "SSEXXX",
            "XXXXXE",
            "WXSXXX",
        ],
        "start" : [2, 0],
        "end" : [3, 1]
    }
]
currentLevel : int
grid : list
size : int
start: list
end : list
endLimits : list
gridCoordinate : int
gridWidth : int
marble : list
direction : str
moving : bool
gameover : bool
success : bool
first : bool

def changeLevel(level : int) -> None :
    global currentLevel, grid, size, start, end, endLimits, gridCoordinate, gridWidth, marble, direction, moving, gameover, success, first
    currentLevel = level
    size = levels[currentLevel]["size"]
    grid = levels[currentLevel]["grid"]
    start = levels[currentLevel]["start"]
    end = levels[currentLevel]["end"]
    gridWidth = size * 8 + 1
    gridCoordinate = 64 - gridWidth // 2
    endLimits = [gridCoordinate + 1 + end[0] * 8, gridCoordinate + 1 + end[0] * 8 + 6, gridCoordinate + 1 + end[1] * 8, gridCoordinate + 1 + end[1] * 8 + 6]
    marble = [gridCoordinate + 1 + start[0] * 8 + 3, gridCoordinate + 1 + start[1] * 8 + 3, 3]
    direction = ""
    moving = False
    gameover = False
    success = False
    first = True

def update() -> None :
    global direction, moving, marble, gameover, success, endLimits, currentLevel, first

    if not gameover :

        # La bille est à l'arrêt, on attend que le joueur appuie sur une touche
        if not moving :
            if pyxel.btnp(pyxel.KEY_UP) and pyxel.pget(marble[0], marble[1] - 4) != 10 :
                moving = True
                direction = "N"
            elif pyxel.btnp(pyxel.KEY_RIGHT) and pyxel.pget(marble[0] + 4, marble[1]) != 10 :
                moving = True
                direction = "E"
            elif pyxel.btnp(pyxel.KEY_DOWN) and pyxel.pget(marble[0], marble[1] + 4) != 10 :
                moving = True
                direction = "S"
            elif pyxel.btnp(pyxel.KEY_LEFT) and pyxel.pget(marble[0] - 4, marble[1]) != 10 :
                moving = True
                direction = "W"
        
        # La bille roule inéxorablement jusqu'à... 
        if moving : 
            first = False
            # ...tomber dans le trou d'arrivée
            if endLimits[0] < marble[0] < endLimits[1] and endLimits[2] < marble[1] < endLimits[3] :
                success = True
                marble[2] -= 1
            # Fin de la chute de la bille
            if marble[2] == 0 :
                gameover = True
                moving = False
                direction = ""
            elif direction == "N" :
                # ...tomber du plateau
                if pyxel.pget(marble[0], marble[1] + 4) == 7 :
                    marble[2] -= 1
                else :
                    marble[1] -= 1
                # ...toucher un mur 
                if pyxel.pget(marble[0], marble[1] - 4) == 10 :
                    moving = False
                    direction = ""
            elif direction == "E" :
                # ...tomber du plateau
                if pyxel.pget(marble[0] - 4, marble[1]) == 7  :
                    marble[2] -= 1
                else :
                    marble[0] += 1
                # ...toucher un mur 
                if pyxel.pget(marble[0] + 4, marble[1]) == 10 :
                    moving = False
                    direction = ""
            elif direction == "S" :
                # ...tomber du plateau
                if pyxel.pget(marble[0], marble[1] - 4) == 7  :
                    marble[2] -= 1
                else :
                    marble[1] += 1
                # ...toucher un mur 
                if pyxel.pget(marble[0], marble[1] + 4) == 10 :
                    moving = False
                    direction = ""
            elif direction == "W" :
                # ...tomber du plateau
                if pyxel.pget(marble[0] + 4, marble[1]) == 7  :
                    marble[2] -= 1
                else :
                    marble[0] -= 1
                # ...toucher un mur 
                if pyxel.pget(marble[0] - 4, marble[1]) == 10 :
                    moving = False
                    direction = ""
    else :
        # Victoire ou défaite , on attend que l'utilisateur appuie sur Entrée ou Espace
        if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE) :
            if success :
                if currentLevel + 1 == len(levels):
                    pyxel.quit()
                else :
                    currentLevel += 1
            changeLevel(currentLevel)

def draw() -> None :
    global currentLevel, levels, grid, size, start, end, gridCoordinate, gridWidth, marble, success, first
    pyxel.cls(7)

    # Affichage du plateau
    pyxel.rect(gridCoordinate, gridCoordinate, gridWidth, gridWidth, 12)

    # On parcourt toutes les cases
    for i in range(size) :
        for j in range(size) :
    
            # Calcul des coordonnées de la case
            x = gridCoordinate + 1 + j * 8
            y = gridCoordinate + 1 + i * 8

            # Afficher la fin
            if [j, i] == end :
                pyxel.circ(x + 3, y + 3, 3, 7)
            
            # On met une barrière en fonction de la direction
            if grid[i][j] == "N" :
                pyxel.line(x, y - 1, x + 6, y - 1, 10)
            elif grid[i][j] == "E" :
                pyxel.line(x + 7, y, x + 7, y + 6, 10)
            elif grid[i][j] == "S" :
                pyxel.line(x, y + 7, x + 6, y + 7, 10)
            elif grid[i][j] == "W" :
                pyxel.line(x - 1, y, x - 1, y + 6, 10)
            
    # La boule
    if marble[2] > 0 :
        pyxel.circ(marble[0], marble[1], marble[2], 8)

        # "Illusion" du mouvement
        if moving and marble[2] == 3 :
            pyxel.line(marble[0] - 1, marble[1] - 3, marble[0] + 1, marble[1] - 3,  15)
            pyxel.line(marble[0] - 2, marble[1] - 2, marble[0] + 2, marble[1] - 2,  15)
            if pyxel.frame_count % 10 < 5 :
                pyxel.line(marble[0] - 1, marble[1] - 2, marble[0] + 1, marble[1] - 2,  14)
            pyxel.pset(marble[0] - 3, marble[1] - 1, 14)
            pyxel.pset(marble[0] + 3, marble[1] - 1, 14)

        pyxel.pset(marble[0] - 2, marble[1] - 1, 7)
        pyxel.pset(marble[0] - 1, marble[1] - 2, 7)

    # Fin du niveau
    if gameover :
        if success :
            if currentLevel + 1 == len(levels):
                message = "Fin du jeu !!!"
            else :
                message = "Victoire !"
        else :    
            message = "Perdu..."
        w = len(message) * 4
        pyxel.rect(62 - w // 2, 2, w + 4, 9, 9)
        pyxel.text(64 - w // 2, 4, message, 0)
    elif first :
        message = "Niveau " + str(currentLevel + 1) + "/" + str(len(levels))
        w = len(message) * 4
        pyxel.rect(62 - w // 2, 2, w + 4, 9, 9)
        pyxel.text(64 - w // 2, 4, message, 0)

changeLevel(0)
pyxel.run(update, draw)