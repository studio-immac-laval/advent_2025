# Jour 1

![Défi](../img/day01.gif)

## Défi

Afficher "Vive le vent..." **caractère** par **caractère**.

## Démarrer

Dans un programme "normal", si on souhaitait afficher un texte caractère par caractère, on ferait une boucle et on afficherait les caractères les uns après les autres en faisant une petite pause entre chaque.

Mais dans un programme Pyxel, c'est la boucle infinie d'appels des fonctions `update()` puis `draw()` qui donne le tempo.

On va donc compter les itérations en les cumulant dans une variable `steps` et afficher à chaque appel de `draw()` autant de caractères que de `steps` comptabilisés.

La fréquence d'appel par défaut est de 30 fps (frames per second), donc 30 `steps` par secondes, donc 30 caractères par secondes. C'est un peu rapide, donc on peu temporiser en ne comptant qu'un `steps` toutes les 2 ou 3 itérations. On affichera donc 2 ou 3 fois de suite le même texte, mais ça ne se verra pas 😉. On utilisera pour cela la variable `pyxel.frame_count`.

```py
import pyxel

pyxel.init(128, 128)

steps = 0

def update() :
    global steps

    # On compte une itération sur 2
    if pyxel.frame_count % 2 == 0 :
        steps += 1 

def draw() :
    global steps

    # On efface l'écran
    pyxel.cls(1)

    # On affiche steps juste pour voir 👁️👁️
    pyxel.text(10, 10, str(steps), 7)

pyxel.run(update, draw)
```

Il ne reste "plus qu'à" afficher le texte.

La méthode est différente en fonction de comment on stocke la chanson en mémoire (et surtout de comment on gère les retours à la ligne 😉) :

```py
# Une chaîne de caractères
song = "Vive le vent,\nVive le vent,\nVive le vent d'hiver\nQui s'en va sifflant, soufflant,\nDans les grands sapins verts...\nHey !\nVive le temps,\nVive le temps,\nVive le temps d'hiver\nBoule de neige et jour de l'an,\nEt bonne annee grand-mere !"

# Un tableau de chaînes de caractères
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
```

## Une solution

🐍 [Voir le fichier](day01.py)

```py
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
```