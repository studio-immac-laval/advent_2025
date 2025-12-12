# Jour 13

![Défi](../img/day13.gif)

## Défi

Créer un jeu du serpent (1/3) : manipuler un serpent avec les touches du clavier.

## Démarrer

Pour simplifier le jeu, il faut que le serpent se déplace sur une grille.

Sur un écran de 128 x 128, des cases de 8 x 8 offrent déjà une belle aire de jeu.

La tête du serpent est donc un carré de 8 x 8 qui se déplace en continu dans la même direction tant qu'on n'appuie sur aucune touche. On commence par coder ça.

A partir de là, deux aspects sont à gérer :

+   Que se passe-t-il quand on touche le bord de l'écran ?

    Dans l'exemple ci-dessous, le serpent réapparaît de l'autre côté.

+   Comment gérer le changement de direction ?

    On sait détecter l'appui sur une touche avec `pyxel.btn(pyxel.KEY_nomDeLaTouche)`. Si on le synchronise avec `pyxel.frame_count` pour n'être pris en compte que toutes les 8 itérations, on donnera l'impression d'une grille.

Il ne reste qu'à gérer le corps du serpent... Le corps devra s'agrandir d'un bloc de 8 x 8 à chaque fois que le serpent mangera une pomme. Sa longueur est donc une variable.

Une solution simple (mais qu'on ne gardera peut-être pas pour la suite) est de sauvegarder les 8 x longueur dernières positions de la tête, puis d'afficher un carré de 8 x 8 à chacune de ces positions. Pas élégant ni économe mais efficace pour une première version.

## Une solution

🐍 [Voir le fichier](day13.py)

```py
import pyxel

pyxel.init(128, 128)

DIRECTION_NORTH = 0
DIRECTION_EAST = 1
DIRECTION_SOUTH = 2
DIRECTION_WEST = 3

# Création du serpent
# On utilise un dictionnaire pour regrouper toutes ses informations :
snake = {
    "x" : 64,                       # Abscisse de la tête
    "y" : 64,                       # Ordonnée de la tête
    "length" : 5,                   # Taille du serpent (en bloc de 8 x 8)
    "direction" : DIRECTION_NORTH,  # Direction de l'avancée
    "previous" : [[64, 64]]         # Historique des positions de la tête
}

def update() :
    global snake
    
    # Sauvegarde "sommaire" de la position
    snake["previous"].append([snake["x"], snake["y"]])
    if len(snake["previous"]) > snake["length"] * 8 :
        snake["previous"].pop(0)

    # Changement de direction (mais pas de demi-tour !)
    # Pris en compte toutes les 8 frames pour donner une impression de grille
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
```