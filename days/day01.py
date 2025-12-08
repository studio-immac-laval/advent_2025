import pyxel

pyxel.init(128, 128)

song = [
    "Vive le vent,",
    "Vive le vent,",
    "Vive le vent d'hiver",
    "Qui s'en va sifflant, soufflant,",
    "Dans les grands sapins verts...",
    "Hey !",
    " ",
    "Vive le temps,",
    "Vive le temps,",
    "Vive le temps d'hiver",
    "Boule de neige et jour de l'an,",
    "Et bonne annee grand-mere !"
]

steps = 0

def update() :
    global steps

    # On compte une itération sur 2
    if pyxel.frame_count % 2 == 0 :
        steps += 1 

def draw() :
    global steps, song

    # On efface l'écran
    pyxel.cls(1)

    line = 0
    
    # Une variable pour décompter les caractères qu'il nous reste
    remainingChars = steps
    
    while remainingChars > 0 and line < len(song) :
        # Si la ligne actuelle ne contient pas assez de caractère
        # on n'en affiche qu'une partie
        if remainingChars < len(song[line]) :
            pyxel.text(1, 20 + 7 * line, song[line][:remainingChars], 7)
            remainingChars = 0
        
        # sinon on affiche tout et on passe à la ligne suivante
        else :
            pyxel.text(1, 20 + 7 * line, song[line], 7)
            remainingChars -= len(song[line])
            line += 1

pyxel.run(update, draw)