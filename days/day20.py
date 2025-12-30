import pyxel
from random import randint
from math import sqrt

santa : dict
chimneys : list
gameover : bool

def distance(a : dict, b : dict) -> float :
    """
    renvoie la distance entre deux points a et b d'un plan orthogonal
    
    :param a: le point a avec des coordonnées "x" et "y"
    :type a: dict
    :param b: le point b avec des coordonnées "x" et "y"
    :type b: dict
    :return: la distance entre a et b
    :rtype: float
    """
    return sqrt((a["x"] - b["x"])**2 + (a["y"] - b["y"])**2)

def init() :
    global santa, chimneys, gameover

    # Placement initial du Père Noël
    santa = {
        "x" : randint(10, 118),
        "y" : randint(10, 118),
        "target" : -1,
        "visiting" : 0,
        "radius" : 3
    }

    # Placement des cheminées
    chimneys = []
    while len(chimneys) < 10 :
        chimney = {
            "x" : randint(10, 118),
            "y" : randint(10, 118), 
            "visited" : False
        }
        # Pas de cheminées à moins de 30 pixels d'une autre
        if len(chimneys) == 0 :
            chimneys.append(chimney)
        else :
            too_close = False
            i = 0
            while i < len(chimneys) and not too_close :
                if distance(chimney, chimneys[i]) < 30 :
                    too_close = True
                i += 1
            if not too_close :
                chimneys.append(chimney)

    # La tournée commence !
    gameover = False

def update() :
    global santa, chimneys, gameover

    # La tournée n'est pas terminée
    if not gameover :

        # Le Père Noël n'est pas dans une cheminée
        if santa["visiting"] == 0 :

            # Le Père Noël n'a pas de cible
            if santa["target"] == -1 :
                # Quelle cheminée non visitée est la plus proche ?
                min_distance = 182
                for i in range(len(chimneys)) :
                    if not chimneys[i]["visited"] :
                        # Calcul de la distance
                        current_distance = distance(santa, chimneys[i])
                        if  current_distance < min_distance :
                            min_distance = current_distance
                            santa["target"] = i
                
            # Reste-il des cheminées à visiter ?
            if santa["target"] == -1 :
                gameover = True
            else :
                dx = santa["x"] - chimneys[santa["target"]]["x"]
                dy = santa["y"] - chimneys[santa["target"]]["y"]
                # Le Père Noël est arrivé à destination
                if dx == 0 and dy == 0 :
                    # On est arrivé
                    chimneys[santa["target"]]["visited"] = True
                    santa["target"] = -1
                    santa["visiting"] = -1
                # On se rapproche de la cheminée la plus proche
                else :
                    if dx > 0 : dx = -1
                    elif dx < 0 : dx = 1
                    if dy > 0 : dy = -1
                    elif dy < 0 : dy = 1
                    santa["x"] += dx
                    santa["y"] += dy

        else :
            # On entre dans la cheminée (animation)
            santa["radius"] += santa["visiting"]
            if santa["radius"] == 0 :
                santa["visiting"] = 1
            elif santa["radius"] == 3 :
                santa["visiting"] = 0 
    
    else :
        # Réinitialisation
        if pyxel.btn(pyxel.KEY_RETURN) :
            init()
                

def draw() :
    global santa, chimneys
    pyxel.cls(7)

    # Cheminées
    for chimney in chimneys :
        pyxel.rect(chimney["x"] - 3, chimney["y"] - 3, 7, 7, 7 if chimney["visited"] else 0)
        pyxel.rectb(chimney["x"] - 3, chimney["y"] - 3, 7, 7, 9)

    # Santa
    pyxel.circ(santa["x"], santa["y"], santa["radius"], 8)

init()
pyxel.init(128, 128)
pyxel.run(update, draw)