# Jour 15

![Défi](../img/day15.gif)

## Défi

Créer un jeu du serpent (3/3) : une difficulté progressive ?

## Démarrer

Proposons un système de niveau avec de plus en plus de pommes à récupérer, de plus en plus de rochers à éviter, une vitesse de déplacement qui augmente et même une bordure !

On utilise un dictionnaire pour stocker les informations de chaque niveau.

On met à jour le code pour prendre en compte ces éléments.

Quelques réglages pour doser la difficulté et voici 5 niveaux de plus en plus corsés !

## Amélioration

La prise en compte de la touche pressée toutes les 8 frames n'était pas idéale, maintenant on enregistre la dernière touche pressée et on la "joue" à la 8ème frame suivante.

## Une solution

🐍 [Voir le fichier](day15.py)

```py
import pyxel
from random import randint

pyxel.init(128, 128)

DIRECTION_NORTH = 0
DIRECTION_EAST = 1
DIRECTION_SOUTH = 2
DIRECTION_WEST = 3

snake : dict
apples : list
rocks : list
gameover : bool
delay : int
next : int

# Niveaux
levels = [
    {
        "title" : "Tranquille !",
        "rocks" : 10,
        "apples" : 10,
        "speed" : 1,
        "borders" : False
    },
    {
        "title" : "Plus de pommes...",
        "rocks" : 20,
        "apples" : 20,
        "speed" : 1,
        "borders" : False
    },
    {
        "title" : "Des rochers partout !",
        "rocks" : 50,
        "apples" : 20,
        "speed" : 1,
        "borders" : False
    },
    {
        "title" : "Too fast too furious",
        "rocks" : 15,
        "apples" : 10,
        "speed" : 2,
        "borders" : False
    },
    {
        "title" : "Octogone !!!",
        "rocks" : 50,
        "apples" : 20,
        "speed" : 1,
        "borders" : True
    }
]

# Niveau courant
level = 0

def init() :
    global snake, gameover, apples, rocks, delay, level, levels, next

    # Création du serpent
    snake = {
        "x" : 64,
        "y" : 64,
        "length" : 0,
        "direction" : None,
        "previous" : [[64, 64]]
    }

    # Création des pommes
    apples = []
    while len(apples) != levels[level]["apples"] :
        apples.append(str(randint(0, 15) * 8) + "," + str(randint(0, 15) * 8))
        # Dédoublonnage des pommes
        apples = list(set(apples))

    # Création des pierres
    rocks = []
    while len(rocks) != levels[level]["rocks"] :
        rocks.append(str(randint(0, 15) * 8) + "," + str(randint(0, 15) * 8))
        # Dédoublonnage des pierres
        rocks = list(set(rocks))
        # Pas de superposition avec les pommes
        common = (set(rocks)).intersection(set(apples))
        if len(common) > 0 :
            rocks.remove(common.pop())

    # Passage des coordonnées de string en list
    for i in range(len(apples)) :
        apples[i] = list(map(int, apples[i].split(",")))
    for i in range(len(rocks)) :
        rocks[i] = list(map(int, rocks[i].split(",")))

    # Lancement du jeu !
    gameover = False
    next = -1
    delay = pyxel.frame_count

def update() :
    global snake, gameover, apples, rocks, level, next
    
    if not gameover : 
        # Sauvegarde de la position
        snake["previous"].append([snake["x"], snake["y"]])
        if len(snake["previous"]) * levels[level]["speed"] > snake["length"] * 8 :
            snake["previous"].pop(0)

        # Changement de direction (mais pas de demi-tour !)
        if snake["direction"] != DIRECTION_SOUTH and pyxel.btnp(pyxel.KEY_UP) :
            next = DIRECTION_NORTH
        elif snake["direction"] != DIRECTION_NORTH and pyxel.btnp(pyxel.KEY_DOWN) :
            next = DIRECTION_SOUTH
        elif snake["direction"] != DIRECTION_EAST and pyxel.btnp(pyxel.KEY_LEFT) :
            next = DIRECTION_WEST
        elif snake["direction"] != DIRECTION_WEST and pyxel.btnp(pyxel.KEY_RIGHT) :
            next = DIRECTION_EAST
        if (pyxel.frame_count - delay) % 8 == 0 and next != -1 :
            snake["direction"] = next
            next = -1

        # Avancée inexorable
        if snake["direction"] == DIRECTION_EAST :
            snake["x"] += levels[level]["speed"]
        elif snake["direction"] == DIRECTION_WEST :
            snake["x"] -= levels[level]["speed"]
        elif snake["direction"] == DIRECTION_NORTH :
            snake["y"] -= levels[level]["speed"]
        elif snake["direction"] == DIRECTION_SOUTH :
            snake["y"] += levels[level]["speed"]

        # Colision avec le corps ou une pierre 
        if snake["direction"] == DIRECTION_EAST and pyxel.pget(snake["x"] + 7, snake["y"]) in [9, 13] :
            gameover = True
        elif snake["direction"] == DIRECTION_WEST and pyxel.pget(snake["x"], snake["y"]) in [9, 13] :
            gameover = True
        elif snake["direction"] == DIRECTION_NORTH and pyxel.pget(snake["x"], snake["y"]) in [9, 13] :
            gameover = True
        elif snake["direction"] == DIRECTION_SOUTH and pyxel.pget(snake["x"], snake["y"] + 7) in [9, 13] :
            gameover = True

        # Manger une pomme
        try : 
            i = apples.index([snake["x"], snake["y"]])
            apples.pop(i)
            snake["length"] += 1
        except ValueError :
            pass
        if len(apples) == 0 :
            gameover = True
            level += 1

        # Gestion des bords de l'écran
        if levels[level]["borders"] :
            if snake["x"] == 128 or snake["x"] == -1 or snake["y"] == 128 or snake["y"] == -1 :
                gameover = True
        else :
            if snake["x"] == -4 :
                snake["x"] = 124
            elif snake["x"] == 124 :
                snake["x"] = -4
            elif snake["y"] == -4 :
                snake["y"] = 124
            elif snake["y"] == 124 :
                snake["y"] = -4
    
    else :
        if (pyxel.btn(pyxel.KEY_RETURN)) :
            init()
            update()

def draw() :
    global snake, level, levels
    pyxel.cls(0)

    # Affichage des bordures
    if not gameover and levels[level]["borders"] :
        pyxel.rectb(0, 0, 128, 128, 10)

    # Affichage des pommes
    for i in range(len(apples)) :
        pyxel.rect(apples[i][0], apples[i][1], 8, 8, 8)

    # Affichage des pierres
    for i in range(len(rocks)) :
        pyxel.rect(rocks[i][0], rocks[i][1], 8, 8, 13)

    # Affichage du serpent
    for i in range(len(snake["previous"])) :
        pyxel.rect(snake["previous"][i][0], snake["previous"][i][1], 8, 8, 9)

    # Affichage du niveau
    if snake["direction"] == None :
        pyxel.rect(47, 29, 32, 7, 2)
        pyxel.text(48, 30, "NIVEAU " + str(level + 1), 7)
        # Titre
        length = len(levels[level]["title"]) * 4
        x = 64 - length // 2
        pyxel.rect(x - 1, 36, length + 1, 8, 2)
        pyxel.text(x, 37, levels[level]["title"], 7)

    # Game over
    if gameover :
        if len(apples) == 0 :
            pyxel.rect(43, 60, 36, 7, 2)
            pyxel.text(44, 61, "VICTOIRE!", 7)
        else : 
            pyxel.rect(43, 60, 36, 7, 2)
            pyxel.text(44, 61, "GAME OVER", 7)

init()
pyxel.run(update, draw)
```