# Jour 17

![Défi](../img/day17.gif)

## Défi

Créer un jeu de labyrinthe (1/2).

On joue avec une bille et on doit emmener cette bille jusqu'au trou.

Une fois qu'on imprime une direction à la bille, elle roule jusqu'à rencontrer un mur ou tomber dans le vide.

## Démarrer

La première partie de ce défi consiste à créer un système capable de dessiner des plateaux de jeu.

Pour cela, on crée une structure de données qui permet de stocker les différentes informations d'un niveau de jeu en partant des hypothèses suivantes : 

+   le plateau est carré,

+   le plateau est une grille,

+   on peut placer un mur entre les cases de la grille,

La structure de données `levels` est une liste qui contient des dictionnaires qui contiennent les informations suivantes :

+   `size` : le nombre de cases d'un côté de la grille

+   `grid` : le plan du plateau sous la forme d'un tableau de chaînes de caractères. 
    
    Chaque chaîne correspond à une ligne, chaque caractère à une case. 
    
    Les valeurs N, E, S, W correspondent au placement du mur sur la case. X indique qu'il n'y a pas de mur sur la case.

+   `start` : les coordonnées de la case de départ dans la grille (indexées à 0)

+   `end` : les coordonnées de la case de fin dans la grille (indexées à 0)

## Une solution

🐍 [Voir le fichier](day17.py)

```py
import pyxel
from random import randint

pyxel.init(128, 128)

# Liste des niveaux

# Chaque niveau est décrit par :
# + size : le nombre de cases d'un côté plateau
# + grid : La grille du plateau
# + start : La case de départ
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
            "XXXWN",
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

def changeLevel(level : int) -> None :
    global currentLevel, grid, size, start, end, endLimits, gridCoordinate, gridWidth, ball, direction, moving, gameover, success, first
    currentLevel = level
    size = levels[currentLevel]["size"]
    grid = levels[currentLevel]["grid"]
    start = levels[currentLevel]["start"]
    end = levels[currentLevel]["end"]
    gridWidth = size * 8 + 1
    gridCoordinate = 64 - gridWidth // 2

def update() -> None :
    global currentLevel

    # Affiche tous les niveaux
    if pyxel.frame_count % 45 == 0 :
        currentLevel += 1 
        if currentLevel > len(levels) - 1 :
            currentLevel = 0
        changeLevel(currentLevel)

def draw() -> None :
    global currentLevel, levels, grid, size, start, end, gridCoordinate, gridWidth
    pyxel.cls(7)

    # Affichage du plateau
    pyxel.rect(gridCoordinate, gridCoordinate, gridWidth, gridWidth, 12)

    # On parcourt toutes les cases
    for i in range(size) :
        for j in range(size) :
    
            # Calcul des coordonnées de la case
            x = gridCoordinate + 1 + j * 8
            y = gridCoordinate + 1 + i * 8

            # Afficher le début
            if [j, i] == start :
                pyxel.circ(x + 3, y + 3, 3, 8)

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
            
    # Affichage du numéro du niveau
    message = "Niveau " + str(currentLevel + 1) + "/" + str(len(levels))
    w = len(message) * 4
    pyxel.rect(62 - w // 2, 2, w + 4, 9, 9)
    pyxel.text(64 - w // 2, 4, message, 0)

currentLevel = 0
pyxel.run(update, draw)
```